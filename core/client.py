# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import os
import sys
import logging
import time
from pyrogram import Client

# Impor konfigurasi dari file config.py
from config import (
    API_ID,
    API_HASH,
    BOT_TOKEN,
    OWNER_ID,
    PREFIX,
    SESSION_STRING,
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
            name="VzoelUbot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION_STRING,
            bot_token=BOT_TOKEN,
            workers=24,
            sleep_threshold=180,
        )
        self.LOGGER = LOGGER
        self.owner_id = OWNER_ID
        self.prefix = PREFIX
        self.start_time = time.time()

    async def start(self):
        """Memulai client userbot dan mencetak pesan status."""
        await super().start()
        self.LOGGER.info("Userbot telah berhasil dimulai.")

    async def stop(self):
        """Menghentikan client userbot."""
        await super().stop()
        self.LOGGER.info("Userbot telah berhasil dihentikan.")
