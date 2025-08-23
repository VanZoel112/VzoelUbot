# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import asyncio
import importlib
import logging
from pathlib import Path
from pyrogram import idle

from core.client import VzoelUbot
from core.database import initialize_database, get_setting, set_setting
from config import PREFIX as DEFAULT_PREFIX

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

async def load_plugins(app: VzoelUbot):
    """Memuat semua plugin dari folder /plugins."""
    plugins_path = Path("plugins")
    if not plugins_path.is_dir():
        LOGGER.warning("Folder 'plugins' tidak ditemukan. Melewati pemuatan plugin.")
        return
    
    app.loaded_plugins = []
    # ... (Sisa logika pemuat plugin)

async def main():
    """Fungsionalitas utama untuk menjalankan userbot."""
    LOGGER.info("Memulai proses inisialisasi Userbot...")
    
    if not await initialize_database():
        LOGGER.error("Gagal menginisialisasi database. Userbot tidak dapat dimulai.")
        return

    bot_prefix = await get_setting("BOT_PREFIX")
    if bot_prefix is None:
        app_prefix = DEFAULT_PREFIX
        await set_setting("BOT_PREFIX", app_prefix)
    else:
        app_prefix = bot_prefix

    app = VzoelUbot(prefix=app_prefix)
    
    try:
        await app.start()
        await load_plugins(app)
        
        user_info = await app.get_me()
        LOGGER.info(f"User Akun: {user_info.first_name} (@{user_info.username or 'N/A'})")

        LOGGER.info("Userbot sekarang online. Menunggu perintah...")
        await idle()
        
    except (KeyboardInterrupt, SystemExit):
        LOGGER.info("Menerima sinyal berhenti...")
    finally:
        LOGGER.info("Menghentikan Userbot...")
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
