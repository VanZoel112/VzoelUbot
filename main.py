# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import asyncio
import uvloop
from pyrogram import idle

from core.client import VzoelUbot
from core.database import initialize_database

# Menginstal uvloop untuk performa asyncio yang lebih baik
uvloop.install()

async def main():
    """Fungsi utama untuk menginisialisasi dan menjalankan userbot."""
    print("[INFO] Memulai proses inisialisasi Userbot...")
    
    # Inisialisasi database
    db_status = await initialize_database()
    if not db_status:
        print("[ERROR] Gagal menginisialisasi database. Userbot tidak dapat dimulai.")
        return

    # Inisialisasi client Telegram
    app = VzoelUbot()
    
    try:
        print("[INFO] Menjalankan Userbot...")
        await app.start()
        
        # Mendapatkan info bot dan user
        bot_info = await app.get_me()
        print(f"[INFO] Berhasil masuk sebagai Bot: {bot_info.first_name} (@{bot_info.username})")
        
        user_info = await app.get_users("me")
        print(f"[INFO] User Akun: {user_info.first_name} (@{user_info.username})")

        print("[INFO] Userbot sekarang online. Menunggu perintah...")
        await idle()
        
    except Exception as e:
        print(f"[FATAL ERROR] Terjadi kesalahan saat menjalankan Userbot: {e}")
    finally:
        print("[INFO] Menghentikan Userbot...")
        await app.stop()
        print("[INFO] Userbot telah berhenti.")

if __name__ == "__main__":
    asyncio.run(main())
