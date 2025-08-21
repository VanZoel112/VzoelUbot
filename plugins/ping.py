# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import time
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.types import Message

# Mengimpor komponen inti dari arsitektur kita
from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only

# --- Daftar Kata untuk Animasi ---
# Anda bisa menambah atau mengubah kata-kata ini sesuka hati.
PROCESSING_WORDS = [
    "Pinging...",
    "Menghubungi server Telegram...",
    "Menghitung latensi...",
    "Memverifikasi koneksi...",
    "Sedang dalam proses...",
    "Hampir selesai...",
]


@VzoelUbot.on_message(filters.command("ping", PREFIX) & filters.me)
@owner_only
async def ping_command(client: VzoelUbot, message: Message):
    """
    Fungsi ini merespons perintah .ping untuk mengukur latensi
    dengan animasi respons.
    """
    start_time = time.time()
    
    # Memilih dua kata acak dari daftar untuk animasi
    animation_words = random.sample(PROCESSING_WORDS, 2)
    
    try:
        # Loop animasi
        for word in animation_words:
            await message.edit_text(word)
            await asyncio.sleep(0.5) # Jeda 0.5 detik antar editan

    except Exception:
        # Jika ada error (misal: pesan dihapus), proses akan berhenti tanpa crash.
        return

    end_time = time.time()
    latency = round((end_time - start_time) * 1000, 2)
    
    # Mengedit pesan sekali lagi untuk menampilkan hasil latensi final
    await message.edit_text(f"**Pong!**\n`Latensi: {latency} ms`")
