# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from pyrogram.types import Message

def get_user(message: Message) -> str:
    """Mendapatkan string representasi pengguna dari sebuah pesan."""
    if message.from_user:
        user = message.from_user
        return f"{user.first_name} (ID: {user.id})"
    elif message.sender_chat:
        chat = message.sender_chat
        return f"{chat.title} (ID: {chat.id})"
    return "Pengguna Anonim"

# Anda bisa menambahkan fungsi-fungsi bantuan lain di sini di masa depan.
# Contoh: def format_time(seconds), def clean_text(text), dll.
