# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from pyrogram import Client, filters
from pyrogram.types import Message

from core.client import VzoelUbot
from config import PREFIX as DEFAULT_PREFIX
from core.decorators import owner_only
from core.database import set_setting

@VzoelUbot.on_message(filters.command("setprefix", DEFAULT_PREFIX) & filters.me)
@owner_only
async def set_prefix_command(client: VzoelUbot, message: Message):
    """
    Mengatur prefix perintah baru.
    Penggunaan: .setprefix [prefix_baru]
    """
    args = message.text.split(None, 1)
    
    # Jika hanya .setprefix, tampilkan prefix saat ini
    if len(args) == 1:
        # Mengambil prefix dari instance client yang sedang berjalan
        current_prefix = client.prefix if client.prefix else "none"
        return await message.edit_text(f"Prefix saat ini adalah: `{current_prefix}`")

    # Mengambil prefix baru dari argumen
    new_prefix = args[1].strip()

    # Menyimpan prefix baru ke database
    await set_setting("BOT_PREFIX", new_prefix)
    
    await message.edit_text(
        f"Prefix telah diubah menjadi: `{new_prefix}`\n\n"
        "**Harap hidupkan ulang (*restart*) bot agar perubahan ini aktif.**"
  )
