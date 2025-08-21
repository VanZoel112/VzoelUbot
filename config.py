# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

# config.py (Versi Revisi)

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))

# Menambahkan variabel baru
SESSION_STRING = os.getenv("SESSION_STRING", "")

# Memastikan variabel krusial terisi
if not SESSION_STRING:
    print("[FATAL ERROR] SESSION_STRING tidak ditemukan. Harap generate dan masukkan di file .env")
    exit(1)
