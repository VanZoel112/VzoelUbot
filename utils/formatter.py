# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from typing import List, Dict, Any

# --- Koleksi Emoji Standar ---
# Kita bisa memusatkan emoji di sini untuk konsistensi.
EMOJIS = {
    "proses": "⏳",
    "sukses": "✅",
    "gagal": "❌",
    "peringatan": "⚠️",
    "info": "ℹ️",
}

def format_header(title: str) -> str:
    """Membuat header standar untuk pesan."""
    return f"**✦ {title.upper()} ✦**\n\n"

def format_dict_to_list(data: Dict[str, Any]) -> str:
    """Mengubah dictionary menjadi daftar string yang diformat."""
    response = ""
    for key, value in data.items():
        # Mengubah key menjadi format yang lebih rapi (contoh: 'owner_id' -> 'Owner ID')
        formatted_key = key.replace("_", " ").title()
        response += f"• **{formatted_key}:** `{value}`\n"
    return response

def format_error(error_message: str) -> str:
    """Memformat pesan error standar."""
    return f"{EMOJIS['gagal']} **Error:**\n`{error_message}`"

def format_success(success_message: str) -> str:
    """Memformat pesan sukses standar."""
    return f"{EMOJIS['sukses']} {success_message}"

# Contoh penggunaan yang lebih kompleks di masa depan:
# Kita bisa membuat fungsi yang menerima sebuah template dan data,
# lalu secara otomatis mengisi template tersebut.
#
# def render_template(template_name: str, context: Dict[str, Any]) -> str:
#     # Logika untuk memuat template dari assets/messages/ dan mengisinya
#     pass
