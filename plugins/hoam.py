# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

# Mengimpor komponen dari arsitektur kita
from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only

# --- Daftar Kata untuk Animasi Hoam ---
HOAM_ANIMATION = [
    "hoaaammm membosankan",
    "sebel",
    "gabut",
    "pengen makan orang",
    "gtw cape"
]

@VzoelUbot.on_message(filters.command("hoam", PREFIX) & filters.me)
@owner_only
async def hoam_command(client: VzoelUbot, message: Message):
    """
    Perintah ini menjalankan animasi teks 'hoam'.
    """
    try:
        # Loop animasi, mengedit pesan sesuai daftar kata
        for text in HOAM_ANIMATION:
            await message.edit_text(text)
            await asyncio.sleep(0.5) # Jeda 0.5 detik antar editan
    except Exception as e:
        # Log error jika terjadi masalah (misal: pesan dihapus)
        client.LOGGER.error(f"Error di .hoam: {e}")
