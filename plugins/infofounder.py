# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from pyrogram import Client, filters
from pyrogram.types import Message

# Mengimpor komponen dari arsitektur kita
from core.client import VzoelUbot
from config import PREFIX
from core.decorators import owner_only

# --- Teks Info Founder ---
# Seluruh teks yang Anda berikan disimpan di sini.
# Tanda ``` di awal dan akhir akan membuatnya menjadi monospaced di Telegram.
FOUNDER_INFO_TEXT = """
<code>✦━━━━━━━ VZOEL ASSISTANT ━━━━━━━✦
#         ⚡ Founder Information ⚡
# ────────────────────────────────

FOUNDER_USERBOT = "👑 Vzoel Fox's (Lutpan)"
FOUNDER_IG      = "📸 -"
FOUNDER_ID      = "🆔 -"

# 📝 NOTE :
# Repo ini dibuat dari 0, tanpa fork dari userbot lain.
# Dibangun dengan Pyrogram v1 & v2, full Python.
# Harap gunakan bot ini dengan bijak:
#  • Jaga STRING_SESSION, API_ID, dan API_HASH
#  • Agar mudah login kembali jika force logout
#
# ✦ Hvfun 'n Enjoy ✦
# 🛑 #stopjudol
#
# ────────────────────────────────
#   ©2025 ~ Vzoel Fox's
# ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
</code>
"""

@VzoelUbot.on_message(filters.command("founder", PREFIX) & filters.me)
@owner_only
async def founder_info_command(client: VzoelUbot, message: Message):
    """
    Perintah ini menampilkan informasi tentang founder.
    """
    # Mengedit pesan perintah asli dengan teks info yang sudah kita siapkan.
    await message.edit_text(
        FOUNDER_INFO_TEXT,
        disable_web_page_preview=True
    )
