# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from pyrogram import Client, filters
from pyrogram.types import Message

# Mengimpor komponen dari arsitektur kita
from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only
from core.database import (
    add_to_blacklist,
    remove_from_blacklist,
    get_blacklist,
)

@VzoelUbot.on_message(filters.command("blacklist", PREFIX) & filters.me)
@owner_only
async def blacklist_command(client: VzoelUbot, message: Message):
    """
    Menambahkan sebuah chat ke dalam daftar hitam (blacklist).
    Penggunaan: .blacklist <chat_id> [alasan]
    """
    args = message.text.split()
    if len(args) < 2:
        return await message.edit_text("`Penggunaan: .blacklist <chat_id> [alasan]`")

    try:
        chat_id = int(args[1])
        reason = " ".join(args[2:]) if len(args) > 2 else "Tidak ada alasan."
        
        await add_to_blacklist(chat_id, reason)
        await message.edit_text(f"Berhasil menambahkan `{chat_id}` ke daftar hitam.")
        
    except ValueError:
        await message.edit_text("`Chat ID harus berupa angka.`")
    except Exception as e:
        await message.edit_text(f"**Error:** `{e}`")


@VzoelUbot.on_message(filters.command("unblacklist", PREFIX) & filters.me)
@owner_only
async def unblacklist_command(client: VzoelUbot, message: Message):
    """
    Menghapus sebuah chat dari daftar hitam.
    Penggunaan: .unblacklist <chat_id>
    """
    args = message.text.split()
    if len(args) < 2:
        return await message.edit_text("`Penggunaan: .unblacklist <chat_id>`")
        
    try:
        chat_id = int(args[1])
        
        await remove_from_blacklist(chat_id)
        await message.edit_text(f"Berhasil menghapus `{chat_id}` dari daftar hitam.")

    except ValueError:
        await message.edit_text("`Chat ID harus berupa angka.`")
    except Exception as e:
        await message.edit_text(f"**Error:** `{e}`")


@VzoelUbot.on_message(filters.command("listbl", PREFIX) & filters.me)
@owner_only
async def list_blacklist_command(client: VzoelUbot, message: Message):
    """
    Menampilkan semua chat yang ada di daftar hitam.
    """
    await message.edit_text("`Mengambil data daftar hitam...`")
    
    blacklisted_chats = await get_blacklist()
    
    if not blacklisted_chats:
        return await message.edit_text("Daftar hitam kosong.")
        
    response_text = "**Daftar Hitam Gcast:**\n\n"
    for item in blacklisted_chats:
        reason = item.get("reason", "N/A")
        response_text += f"• **ID:** `{item['chat_id']}`\n   **Alasan:** `{reason}`\n"
        
    await message.edit_text(response_text)
