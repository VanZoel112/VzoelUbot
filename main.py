# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)
# main.py (VERSI REVISI FINAL)

import asyncio
import importlib
import logging
from pathlib import Path
from pyrogram import idle

from core.client import VzoelUbot
from core.database import initialize_database, get_setting, set_setting
from core.string_manager import load_strings
from config import PREFIX as DEFAULT_PREFIX

# Menggunakan uvloop jika tersedia untuk performa tinggi
try:
    import uvloop
    uvloop.install()
    logging.info("Menggunakan event loop uvloop (Performa Tinggi).")
except ImportError:
    logging.info("uvloop tidak ditemukan. Menggunakan event loop asyncio standar.")
    pass

# Setup logging dasar
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
        app.loaded_plugins = []
        return
    
    LOGGER.info("Memulai pemindaian plugins...")
    
    app.loaded_plugins = []
    for file in plugins_path.glob("*.py"):
        if file.name.startswith("_"):
            continue
        
        plugin_name = file.stem
        try:
            importlib.import_module(f"plugins.{plugin_name}")
            LOGGER.info(f"[OK] Plugin '{plugin_name}' berhasil dimuat.")
            app.loaded_plugins.append(plugin_name)
        except Exception as e:
            LOGGER.error(f"[FAIL] Gagal memuat plugin '{plugin_name}': {e}")
            
    LOGGER.info(f"Total {len(app.loaded_plugins)} plugin berhasil dimuat.")


async def main():
    """Fungsionalitas utama untuk menginisialisasi dan menjalankan userbot."""
    
    # Memuat semua string dari file JSON sebelum hal lain
    load_strings()

    LOGGER.info("Memulai proses inisialisasi Userbot...")
    
    if not await initialize_database():
        LOGGER.error("Gagal menginisialisasi database. Userbot tidak dapat dimulai.")
        return

    # Memuat prefix dari database, jika ada. Jika tidak, gunakan dari config.
    bot_prefix = await get_setting("BOT_PREFIX")
    if bot_prefix is None:
        app_prefix = DEFAULT_PREFIX
        await set_setting("BOT_PREFIX", app_prefix)
    else:
        app_prefix = bot_prefix

    # Memberikan prefix ke client saat inisialisasi
    app = VzoelUbot(prefix=app_prefix)
    
    try:
        await app.start()
        
        user_info = await app.get_me()
        LOGGER.info(f"User Akun: {user_info.first_name} (@{user_info.username or 'N/A'})")
        LOGGER.info(f"Menggunakan Prefix: '{app.prefix}'")

        await load_plugins(app)

        LOGGER.info("Userbot sekarang online. Menunggu perintah...")
        await idle()
        
    except (KeyboardInterrupt, SystemExit):
        LOGGER.info("Menerima sinyal berhenti...")
    except Exception as e:
        LOGGER.fatal(f"Terjadi kesalahan fatal saat menjalankan Userbot: {e}", exc_info=True)
    finally:
        LOGGER.info("Menghentikan Userbot...")
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
