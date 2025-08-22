# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)
# main.py (VERSI REVISI FINAL)

import asyncio
import importlib
import logging
from pathlib import Path
from pyrogram import idle

from core.client import VzoelUbot
from core.database import initialize_database

# ... (Blok uvloop dan setup logging tetap sama) ...

async def load_plugins(app: VzoelUbot):
    """Fungsi untuk memuat semua plugin dari folder /plugins."""
    plugins_path = Path("plugins")
    
    # --- PERBAIKAN DITERAPKAN DI SINI ---
    if not plugins_path.is_dir():
        LOGGER.warning("Folder 'plugins' tidak ditemukan. Melewati pemuatan plugin.")
        return
    # ------------------------------------

    LOGGER.info("Memulai pemindaian plugins...")
    
    app.loaded_plugins = []
    for file in plugins_path.glob("*.py"):
        if file.name == "__init__.py":
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
    # ... (Sisa kode di dalam fungsi main() tetap sama persis) ...
    LOGGER.info("Memulai proses inisialisasi Userbot...")
    
    db_status = await initialize_database()
    if not db_status:
        LOGGER.error("Gagal menginisialisasi database. Userbot tidak dapat dimulai.")
        return

    app = VzoelUbot()
    
    try:
        LOGGER.info("Menjalankan Userbot...")
        await app.start()
        await load_plugins(app)
        
        bot_info = await app.get_me()
        LOGGER.info(f"Berhasil masuk sebagai Bot: {bot_info.first_name} (@{bot_info.username})")
        
        user_info = await app.get_users("me")
        LOGGER.info(f"User Akun: {user_info.first_name} (@{user_info.username})")

        LOGGER.info("Userbot sekarang online. Menunggu perintah...")
        await idle()
        
    except (KeyboardInterrupt, SystemExit):
        LOGGER.info("Menerima sinyal berhenti...")
    except Exception as e:
        LOGGER.fatal(f"Terjadi kesalahan saat menjalankan Userbot: {e}", exc_info=True)
    finally:
        LOGGER.info("Menghentikan Userbot...")
        await app.stop()
        LOGGER.info("Userbot telah berhenti.")

if __name__ == "__main__":
    asyncio.run(main())
