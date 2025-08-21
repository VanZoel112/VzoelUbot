# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from pyrogram import Client, filters
from pyrogram.types import Message

# Mengimpor komponen dari arsitektur kita
from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only
from core.helpers import get_uptime  # Mengimpor helper baru kita

# --- Variabel Konfigurasi untuk Plugin Alive ---
# PENTING: Ganti dengan URL gambar Telegraph Anda yang sebenarnya.
ALIVE_IMAGE_URL = "https://telegra.ph/file/xxxxxxxxxxxxxxxxxxxxxxxxx.jpg"
BOT_VERSION = "0.0.69"


@VzoelUbot.on_message(filters.command("alive", PREFIX) & filters.me)
@owner_only
async def alive_command(client: VzoelUbot, message: Message):
    """
    Perintah ini mengirimkan pesan status 'alive' dengan detail bot.
    """
    # Mengambil info user dari sesi
    me = await client.get_me()
    
    # Menghitung durasi aktif menggunakan helper
    uptime = get_uptime(client.start_time)
    
    # Membuat teks caption sesuai dengan permintaan Anda
    caption_text = (
        "꧁☬×º°”˜`”°º× 𝑽𝒛𝒐𝒆𝒍 𝑭𝒐𝒙'𝒔 𝒂𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 ×º°”˜`”°º×☬꧂\n\n"
        f"**Founder Ubot :** Vzoel fox's\n"
        f"**Onwer :** [{me.first_name}](tg://user?id={me.id})\n"
        f"**Durasi :** `{uptime}`\n"
        f"**Versi :** `{BOT_VERSION}`\n"
        "**Pyrogram with Python language**\n\n"
        "~©2025 Vzoel (Lutpan)"
    )
    
    # Menghapus pesan perintah asli (.alive)
    await message.delete()
    
    # Mengirim foto dengan caption yang telah kita buat
    await client.send_photo(
        chat_id=message.chat.id,
        photo=ALIVE_IMAGE_URL,
        caption=caption_text
    )
