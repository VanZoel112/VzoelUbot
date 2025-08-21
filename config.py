# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)
# config.py (VERSI FINAL & BERSIH)

import os
from dotenv import load_dotenv

# Muat variabel dari file .env
load_dotenv()

# --- Konfigurasi Wajib ---
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
PREFIX = os.getenv("PREFIX", ".")

# --- Konfigurasi Opsional ---
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))

# --- Validasi Kritis ---
if not API_ID or not API_HASH:
    print("[FATAL ERROR] API_ID atau API_HASH tidak ditemukan. Harap isi di file .env")
    exit(1)

if not SESSION_STRING:
    print("[FATAL ERROR] SESSION_STRING tidak ditemukan. Harap generate dan masukkan di file .env")
    exit(1)

if not OWNER_ID:
    print("[FATAL ERROR] OWNER_ID tidak ditemukan. Harap isi di file .env")
    exit(1)
