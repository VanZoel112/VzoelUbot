# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from functools import wraps
from pyrogram.types import Message
from config import OWNER_ID

def owner_only(func):
    """
    Decorator untuk membatasi sebuah perintah agar hanya bisa digunakan oleh OWNER_ID.
    """
    @wraps(func)
    async def wrapper(client, message: Message, *args, **kwargs):
        # Memeriksa apakah ID pengguna yang mengirim pesan sama dengan OWNER_ID di config
        if message.from_user and message.from_user.id == OWNER_ID:
            # Jika ya, jalankan fungsi perintahnya
            return await func(client, message, *args, **kwargs)
        else:
            # Jika tidak, kirim pesan penolakan dan jangan jalankan perintahnya
            await message.reply_text("Hanya Sang Arsitek yang bisa menggunakan perintah ini.")
    return wrapper

# Anda bisa menambahkan decorator lain di sini, misalnya @admin_only, dll.
