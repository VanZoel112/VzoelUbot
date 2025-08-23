# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import aiosqlite
import os
from typing import List, Dict, Any
from datetime import datetime

DB_PATH = "data/vzoelubot.db"

async def initialize_database():
    """Menginisialisasi database dan membuat tabel jika belum ada."""
    try:
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
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
            await db.commit()
        print("[INFO] Database SQLite berhasil diinisialisasi.")
        return True
    except Exception as e:
        print(f"[ERROR] Inisialisasi database SQLite gagal: {e}")
        return False

# ... (Fungsi-fungsi database lainnya: set_setting, get_setting, add_to_blacklist, dll.)
# (Isi lengkap file ini sama seperti revisi terakhir kita yang sudah tangguh)
