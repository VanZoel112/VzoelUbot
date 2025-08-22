# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)
# Arsitektur Database Revisi Final: SQLite (dengan Auto-Create Directory)

import aiosqlite
import os  # <-- Dependensi baru ditambahkan
from typing import List, Dict, Any
from datetime import datetime

DB_PATH = "data/vzoelubot.db"

async def initialize_database():
    """Menginisialisasi database dan membuat tabel jika belum ada."""
    try:
        # --- PERBAIKAN DITERAPKAN DI SINI ---
        # Secara otomatis membuat folder 'data' jika belum ada.
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        # ------------------------------------

        async with aiosqlite.connect(DB_PATH) as db:
            await db.execute("""
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """)
            await db.execute("""
                CREATE TABLE IF NOT EXISTS blacklist (
                    chat_id INTEGER PRIMARY KEY,
                    reason TEXT,
                    added_at TEXT
                )
            """)
            await db.commit()
        print("[INFO] Database SQLite berhasil diinisialisasi.")
        return True
    except Exception as e:
        print(f"[ERROR] Inisialisasi database SQLite gagal: {e}")
        return False

# --- (Sisa kode di file ini tetap sama persis seperti sebelumnya) ---

async def set_setting(key: str, value: Any):
    """Menyimpan pengaturan atau custom string."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (key.upper(), str(value))
        )
        await db.commit()

async def get_setting(key: str, default: Any = None) -> Any:
    """Mengambil pengaturan atau custom string."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT value FROM settings WHERE key = ?", (key.upper(),))
        row = await cursor.fetchone()
        return row[0] if row else default

async def add_to_blacklist(chat_id: int, reason: str = ""):
    """Menambahkan chat ke blacklist."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT OR REPLACE INTO blacklist (chat_id, reason, added_at) VALUES (?, ?, ?)",
            (chat_id, reason, datetime.utcnow().isoformat())
        )
        await db.commit()

async def remove_from_blacklist(chat_id: int):
    """Menghapus chat dari blacklist."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM blacklist WHERE chat_id = ?", (chat_id,))
        await db.commit()

async def is_blacklisted(chat_id: int) -> bool:
    """Memeriksa apakah sebuah chat ada di dalam blacklist."""
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT 1 FROM blacklist WHERE chat_id = ?", (chat_id,))
        return await cursor.fetchone() is not None

async def get_blacklist() -> List[Dict]:
    """Mengambil semua chat yang ada di blacklist."""
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        cursor = await db.execute("SELECT * FROM blacklist")
        rows = await cursor.fetchall()
        return [dict(row) for row in rows]
