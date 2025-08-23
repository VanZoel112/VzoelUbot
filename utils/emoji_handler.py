# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from typing import Dict, Optional

# --- Database Emoji Kustom ---
# Di masa depan, kita bisa memuat ini dari file assets/emojis/premium.json
# Untuk saat ini, kita definisikan langsung di sini.
CUSTOM_EMOJIS: Dict[str, int] = {
    # Contoh (ganti dengan ID emoji kustom Anda yang sebenarnya):
    # "loading": 5368324170671202246,
    # "success": 5368812612292132371,
    # "failed": 5368822453835206239,
}

def get_emoji(name: str) -> Optional[str]:
    """
    Mengambil emoji kustom berdasarkan nama.
    Akan mengembalikan format yang bisa digunakan oleh Pyrogram jika ditemukan.
    """
    emoji_id = CUSTOM_EMOJIS.get(name.lower())
    if emoji_id:
        # Pyrogram memerlukan format spesifik untuk mengirim emoji kustom
        return f"<emoji id='{emoji_id}'>{name}</emoji>"
    return None

# Contoh fungsi yang lebih canggih untuk masa depan:
#
# EMOJI_FRAMES = {
#     "loading_anim": [
#         5368324170671202246,
#         5368812612292132372,
#         5368822453835206240,
#     ]
# }
#
# def get_emoji_animation(name: str) -> Optional[List[str]]:
#     """Mengambil serangkaian emoji untuk animasi."""
#     frame_ids = EMOJI_FRAMES.get(name.lower())
#     if frame_ids:
#         return [f"<emoji id='{fid}'>{name}</emoji>" for fid in frame_ids]
#     return None
