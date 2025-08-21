# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from main import pytgcalls_client  # Mengimpor klien pytgcalls dari main.py

from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only

# --- Konfigurasi Notifikasi VC ---
# Ganti dengan URL gambar Telegraph dan teks yang Anda inginkan.
VC_IMAGE_URL = "https://telegra.ph/file/xxxxxxxxxxxxxxxxxxxxxxxxx.jpg"
VC_TEXT = "**Vzoel Fox's Assistant** telah memasuki Obrolan Suara."


@VzoelUbot.on_message(filters.command("joinvc", PREFIX) & filters.me & filters.group)
@owner_only
async def join_vc_command(client: VzoelUbot, message: Message):
    """
    Perintah untuk bergabung ke Obrolan Suara dan mengirim notifikasi.
    """
    chat_id = message.chat.id
    await message.delete()

    try:
        await pytgcalls_client.join_group_call(chat_id)
        # Kirim notifikasi yang Anda minta
        await client.send_photo(chat_id, photo=VC_IMAGE_URL, caption=VC_TEXT)
    except Exception as e:
        await client.send_message(chat_id, f"**Error saat bergabung ke VC:**\n`{e}`")


@VzoelUbot.on_message(filters.command("leavevc", PREFIX) & filters.me & filters.group)
@owner_only
async def leave_vc_command(client: VzoelUbot, message: Message):
    """
    Perintah untuk meninggalkan Obrolan Suara.
    """
    chat_id = message.chat.id
    
    try:
        await pytgcalls_client.leave_group_call(chat_id)
        await message.edit_text("Telah berhasil meninggalkan Obrolan Suara.")
        await asyncio.sleep(3)
        await message.delete()
    except Exception as e:
        await message.edit_text(f"**Error saat meninggalkan VC:**\n`{e}`")
