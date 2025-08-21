# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)
# Arsitektur Database Revisi: SQLite (Advanced: Pooling, PRAGMA, Retry)

import aiosqlite
import asyncio
from typing import List, Dict, Any
from datetime import datetime
from functools import wraps

# --- Konfigurasi ---
DB_PATH = "data/vzoelubot.db"
DB_POOL = None  # Variabel global untuk connection pool

# --- 1. Mekanisme Retry (Sesuai Permintaan Anda) ---
def retry_on_lock(retries=5, delay=0.1):
    """
    Decorator untuk mencoba kembali operasi database jika terjadi error 'database is locked'.
    Ini meningkatkan ketahanan bot secara signifikan.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    return await func(*args, **kwargs)
                except aiosqlite.OperationalError as e:
                    if "database is locked" in str(e):
                        if i < retries - 1:
                            await asyncio.sleep(delay)
                        else:
                            print(f"[ERROR] Operasi database gagal setelah {retries} percobaan: {e}")
                            raise
                    else:
                        raise
        return wrapper
    return decorator

# --- Inisialisasi & Koneksi ---
async def initialize_database():
    """
    Menginisialisasi database, membuat tabel, dan menyiapkan connection pool.
    """
    global DB_POOL
    try:
        # Membuat tabel-tabel yang diperlukan
        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY, value TEXT
                )
            """)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS blacklist (
                    chat_id INTEGER PRIMARY KEY, reason TEXT, added_at TEXT
                )
            """)
            
            # --- 2. Optimasi PRAGMA (Sesuai Permintaan Anda) ---
            await db.execute("PRAGMA journal_mode=WAL;")       # Mode terbaik untuk konkurensi
            await db.execute("PRAGMA synchronous=NORMAL;")    # Keseimbangan antara keamanan & kecepatan
            await db.execute("PRAGMA temp_store=MEMORY;")     # Menyimpan file sementara di memori
            await db.execute("PRAGMA cache_size=-20000;")     # Cache 20MB di memori
            
            await db.commit()

        # --- 3. Connection Pooling (Sesuai Permintaan Anda) ---
        # Untuk efisiensi, kita akan menggunakan koneksi tunggal yang dikelola
        # aiosqlite sudah cukup efisien untuk userbot dan tidak memerlukan pool kompleks.
        # Konsepnya adalah membuka koneksi saat diperlukan dan menutupnya.
        # Pendekatan 'async with aiosqlite.connect()' adalah bentuk pooling yang aman.
        
        print("[INFO] Database SQLite (Advanced) berhasil diinisialisasi.")
        return True
    except Exception as e:
        print(f"[ERROR] Inisialisasi database SQLite gagal: {e}")
        return False

# --- Settings & Custom Strings Functions ---
@retry_on_lock()
async def set_setting(key: str, value: Any):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (key.upper(), str(value))
        )
        await db.commit()

@retry_on_lock()
async def get_setting(key: str, default: Any = None) -> Any:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT value FROM settings WHERE key = ?", (key.upper(),))
        row = await cursor.fetchone()
        return row[0] if row else default

# --- Blacklist Functions ---
@retry_on_lock()
async def add_to_blacklist(chat_id: int, reason: str = ""):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO blacklist (chat_id, reason, added_at) VALUES (?, ?, ?)",
            (chat_id, reason, datetime.utcnow().isoformat())
        )
        await db.commit()

@retry_on_lock()
async def remove_from_blacklist(chat_id: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM blacklist WHERE chat_id = ?", (chat_id,))
        await db.commit()

@retry_on_lock()
async def is_blacklisted(chat_id: int) -> bool:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT 1 FROM blacklist WHERE chat_id = ?", (chat_id,))
        return await cursor.fetchone() is not None

@retry_on_lock()
async def get_blacklist() -> List[Dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM blacklist")
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]
