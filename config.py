# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

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

# Prefix awal untuk perintah
PREFIX = os.getenv("PREFIX", ".")