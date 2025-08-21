# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import os
import sys
import logging
import time  # <-- Pastikan 'time' sudah diimpor
from pyrogram import Client

# Impor konfigurasi dari file config.py
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    OWNER_ID,
    PREFIX,
)

# Konfigurasi logging dasar
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)


class VzoelUbot(Client):
    """
    Kelas Userbot utama yang mewarisi dari pyrogram.Client.
    Ini akan menangani inisialisasi client dan memuat semua komponen.
    """
    def __init__(self):
        super().__init__(
            "VzoelUbot",  # Nama sesi
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            # Kita akan menghapus `plugins=` dari sini jika menggunakan pemuat manual
            workers=24,
            sleep_threshold=180,
        )
        self.LOGGER = LOGGER
        self.owner_id = OWNER_ID
        self.prefix = PREFIX
        
        # --- REVISI DITAMBAHKAN DI SINI ---
        # Mencatat waktu mulai bot dengan presisi saat objek diciptakan.
        self.start_time = time.time()
        # ------------------------------------

    async def start(self):
        """Memulai client userbot dan mencetak pesan status."""
        await super().start()
        self.LOGGER.info("Userbot telah berhasil dimulai.")

    async def stop(self):
        """Menghentikan client userbot."""
        await super().stop()
        self.LOGGER.info("Userbot telah berhasil dihentikan.")
