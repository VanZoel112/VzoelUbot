# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from typing import Optional

def is_numeric(value: str) -> bool:
    """
    Memeriksa apakah sebuah string adalah numerik (bisa diubah menjadi integer).
    """
    return value.isdigit() or (value.startswith('-') and value[1:].isdigit())

async def validate_chat_id(chat_id_str: str) -> Optional[int]:
    """
    Memvalidasi dan mengonversi chat_id dari string.
    Mengembalikan integer jika valid, None jika tidak.
    """
    if is_numeric(chat_id_str):
        return int(chat_id_str)
    return None

# Contoh fungsi validator yang lebih kompleks untuk masa depan:
#
# from pyrogram.types import Message
# from pyrogram.errors import PeerIdInvalid
#
# async def can_send_message(client, chat_id: int) -> bool:
#     """
#     Memeriksa apakah bot memiliki izin untuk mengirim pesan ke sebuah chat.
#     """
#     try:
#         await client.send_chat_action(chat_id, "typing")
#         return True
#     except PeerIdInvalid:
#         print(f"[WARNING] Chat ID tidak valid: {chat_id}")
#         return False
#     except Exception as e:
#         print(f"[ERROR] Tidak bisa mengirim ke {chat_id}: {e}")
#         return False
