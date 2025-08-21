# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

# Mengimpor komponen dari arsitektur kita
from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only
from core.database import get_blacklist # Kita butuh ini untuk memeriksa blacklist

# --- Variabel Konfigurasi untuk Gcast ---
# Pesan ini bisa dikustomisasi
ANIMATION_FRAMES = ["...", "...", "...", "...", "..."]
ANIMATION_INTERVAL = 0.3  # Detik


@VzoelUbot.on_message(filters.command("gcast", PREFIX) & filters.me)
@owner_only
async def gcast_command(client: VzoelUbot, message: Message):
    """
    Perintah ini melakukan broadcast pesan ke grup dan supergrup.
    Mode:
    - .gcast <pesan> atau balas pesan: Broadcast normal.
    - .gcast delay <detik> <pesan> atau balas pesan: Broadcast dengan jeda.
    """
    args = message.text.split(None, 1)
    delay_mode = False
    delay_time = 0

    # Memeriksa mode delay
    if len(args) > 1 and args[1].lower().startswith("delay"):
        try:
            delay_parts = args[1].split(None, 2)
            delay_time = int(delay_parts[1])
            delay_mode = True
            # Jika ada pesan setelah delay, gunakan itu. Jika tidak, broadcast pesan yang dibalas.
            if len(delay_parts) > 2:
                message.text = delay_parts[2] # Set ulang teks pesan
            elif not message.reply_to_message:
                return await message.edit_text("Harap balas sebuah pesan atau berikan teks untuk di-broadcast.")
        except (ValueError, IndexError):
            return await message.edit_text("Format delay salah. Gunakan `.gcast delay <detik> <pesan>`.")

    # Menentukan pesan yang akan di-broadcast
    gcast_message = message.reply_to_message if message.reply_to_message else message
    if gcast_message == message and len(args) == 1:
         return await message.edit_text("Harap balas sebuah pesan atau berikan teks untuk di-broadcast.")
    
    # --- Proses Utama Gcast ---
    status_message = await message.edit_text("`Mempersiapkan broadcast...`")
    
    # Mengambil daftar chat
    all_chats = []
    try:
        async for dialog in client.get_dialogs():
            if dialog.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
                all_chats.append(dialog.chat.id)
    except Exception as e:
        return await status_message.edit_text(f"**Error saat mengambil daftar chat:**\n`{e}`")

    # Mengambil daftar blacklist dari database
    blacklist = [item["chat_id"] for item in await get_blacklist()]
    
    # Memfilter chat yang akan di-broadcast
    chats_to_send = [chat for chat in all_chats if chat not in blacklist]
    total_chats = len(chats_to_send)
    
    if total_chats == 0:
        return await status_message.edit_text("Tidak ada grup target (setelah filter blacklist).")

    await status_message.edit_text(
        f"`Memulai broadcast ke {total_chats} grup...`\n"
        f"**Mode:** `{'Delay Spam' if delay_mode else 'Normal'}`\n"
        f"**Jeda:** `{delay_time} detik`" if delay_mode else ""
    )
    await asyncio.sleep(2)

    successful_sends = 0
    failed_sends = 0
    
    # Loop pengiriman pesan
    for i, chat_id in enumerate(chats_to_send):
        # Animasi status
        if i % 5 == 0: # Update status setiap 5 chat
            await status_message.edit_text(
                f"**Broadcast Sedang Berjalan...** {random.choice(ANIMATION_FRAMES)}\n\n"
                f"**Terikirim:** `{successful_sends}`\n"
                f"**Gagal:** `{failed_sends}`\n"
                f"**Progres:** `{i}/{total_chats}`"
            )

        try:
            if gcast_message.text:
                await client.send_message(chat_id, gcast_message.text)
            else: # Jika pesan berisi media (foto, video, stiker)
                await gcast_message.copy(chat_id)

            successful_sends += 1
        except (FloodWait, UserIsBlocked, InputUserDeactivated) as e:
            # Menangani error umum dari Telegram
            failed_sends += 1
            client.LOGGER.warning(f"Gagal mengirim ke {chat_id}: {e}")
        except Exception as e:
            failed_sends += 1
            client.LOGGER.error(f"Error tidak diketahui saat mengirim ke {chat_id}: {e}")

        # Terapkan jeda jika mode delay aktif
        if delay_mode:
            await asyncio.sleep(delay_time)

    # Laporan final
    await status_message.edit_text(
        f"**Broadcast Selesai!**\n\n"
        f"**Total Grup Ditargetkan:** `{total_chats}`\n"
        f"**Berhasil Terkirim:** `{successful_sends}`\n"
        f"**Gagal Terkirim:** `{failed_sends}`"
    )
