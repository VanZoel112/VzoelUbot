# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import logging
import time
from pyrogram import Client

from config import (
    API_ID,
    API_HASH,
    OWNER_ID,
    SESSION_STRING,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)


class VzoelUbot(Client):
    """Kelas Userbot utama."""
    def __init__(self, prefix="."):
        super().__init__(
            name="VzoelUbot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION_STRING,
            workers=24,
            sleep_threshold=180,
        )
        self.LOGGER = LOGGER
        self.owner_id = OWNER_ID
        self.prefix = prefix
        self.start_time = time.time()

    async def start(self):
        await super().start()
        self.LOGGER.info("Userbot telah berhasil dimulai.")

    async def stop(self):
        await super().stop()
        self.LOGGER.info("Userbot telah berhasil dihentikan.")
