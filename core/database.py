# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)
# Arsitektur Database Final: SQLite (Tangguh & Mandiri)

import aiosqlite
import os
from typing import List, Dict, Any
from datetime import datetime

# --- Konfigurasi ---
DB_PATH = "data/vzoelubot.db"

async def initialize_database():
    """
    Menginisialisasi database dan membuat tabel jika belum ada.
    Secara otomatis membuat direktori 'data' jika diperlukan.
    """
    try:
        # Secara otomatis membuat folder 'data' jika belum ada.
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        
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

# --- Settings & Custom Strings Functions ---
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
        return row
