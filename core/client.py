# config.py (Versi Final & Revisi Lengkap)

import os
from dotenv import load_dotenv

# Muat variabel dari file .env ke dalam lingkungan
load_dotenv()

# --- Konfigurasi Krusial ---
# Ambil dari my.telegram.org
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")

# Ambil dari @BotFather di Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# URL koneksi database MongoDB Anda
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

# ID Pengguna Anda (founder/owner)
OWNER_ID = int(os.getenv("OWNER_ID", 0))

# ID Grup untuk log (opsional)
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))

# String Sesi yang dihasilkan dari generate_session.py
SESSION_STRING = os.getenv("SESSION_STRING", "")

# --- BARIS YANG HILANG SEBELUMNYA ---
# Prefix awal untuk perintah, diambil dari .env
PREFIX = os.getenv("PREFIX", ".")
# ------------------------------------


# Memastikan variabel krusial terisi (opsional, tapi praktik baik)
if not API_ID or not API_HASH:
    print("[FATAL ERROR] API_ID atau API_HASH tidak ditemukan. Harap isi di file .env")
    exit(1)

if not SESSION_STRING and not BOT_TOKEN:
    print("[FATAL ERROR] BOT_TOKEN atau SESSION_STRING tidak ditemukan. Salah satu harus diisi.")
    exit(1)
