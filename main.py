# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import asyncio
import importlib
import logging
from pathlib import Path
from pyrogram import idle
from core.client import VzoelUbot
from core.database import initialize_database

# Warna log (optional, pakai colorama)
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
    COLOR = True
except ImportError:
    COLOR = False

# Setup uvloop (jika ada)
try:
    import uvloop
    uvloop.install()
    logging.info("Menggunakan uvloop (performansi tinggi).")
except ImportError:
    logging.info("uvloop tidak ditemukan, fallback ke asyncio.")


class ColorFormatter(logging.Formatter):
    def format(self, record):
        msg = super().format(record)
        if not COLOR:
            return msg
        if record.levelno == logging.INFO:
            return f"{Fore.GREEN}{msg}{Style.RESET_ALL}"
        elif record.levelno == logging.WARNING:
            return f"{Fore.YELLOW}{msg}{Style.RESET_ALL}"
        elif record.levelno == logging.ERROR:
            return f"{Fore.RED}{msg}{Style.RESET_ALL}"
        else:
            return msg


# Setup logging
handler = logging.StreamHandler()
handler.setFormatter(ColorFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
LOGGER.addHandler(handler)


async def load_plugins(app: VzoelUbot):
    """Memuat semua plugin dari folder /plugins."""
    plugins_path = Path("plugins")
    LOGGER.info("Memulai pemindaian plugins...")

    app.loaded_plugins = []
    for file in plugins_path.glob("*.py"):
        if file.name == "__init__.py":
            continue
        try:
            name = f"plugins.{file.stem}"
            importlib.import_module(name)
            app.loaded_plugins.append(name)
            LOGGER.info("✅ Plugin dimuat: %s", file.stem)
        except Exception as e:
            LOGGER.error("❌ Gagal memuat plugin %s: %s", file.stem, e)


async def run_bot():
    """Menjalankan Userbot dengan auto-reconnect + logging warna."""
    app = VzoelUbot()
    await initialize_database()

    while True:
        try:
            await app.start()
            await load_plugins(app)
            LOGGER.info("✅ VzoelUbot berhasil online, menunggu perintah...")
            await idle()
        except Exception as e:
            LOGGER.error("⚠️ Terjadi error: %s", e)
            LOGGER.warning("🔄 Reconnect dalam 5 detik...")
            await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(run_bot())
