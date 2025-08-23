# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")
SESSION_STRING = os.getenv("SESSION_STRING", "")
OWNER_ID = int(os.getenv("OWNER_ID", 0))
PREFIX = os.getenv("PREFIX", ".")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", 0))

if not API_ID or not API_HASH or not SESSION_STRING or not OWNER_ID:
    print("[FATAL ERROR] Harap isi semua variabel wajib di file .env")
    exit(1)
