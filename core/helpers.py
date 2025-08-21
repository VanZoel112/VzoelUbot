# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import time
from datetime import timedelta
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

def get_uptime(start_time: float) -> str:
    """Menghitung dan memformat durasi aktif."""
    now = time.time()
    delta = timedelta(seconds=int(now - start_time))
    
    days = delta.days
    hours, rem = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    uptime_str = ""
    if days > 0:
        uptime_str += f"{days} hari, "
    if hours > 0:
        uptime_str += f"{hours} jam, "
    if minutes > 0:
        uptime_str += f"{minutes} menit, "
    uptime_str += f"{seconds} detik"
    
    return uptime_str
