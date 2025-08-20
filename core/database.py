# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI
from typing import Optional, Dict, Any, Union
from datetime import datetime

# Inisialisasi MongoDB client dan database
client = AsyncIOMotorClient(MONGO_DB_URI)
db = client.VzoelUbotDB

# Mendefinisikan semua koleksi (collections)
settings_collection = db.settings
custom_strings_collection = db.custom_strings
blacklist_collection = db.gcast_blacklist

# --- Settings Functions ---
async def set_setting(key: str, value: Union[bool, str, int]) -> bool:
    """Menyimpan pengaturan ke database."""
    try:
        await settings_collection.update_one(
            {"key": key}, 
            {"$set": {"value": value}}, 
            upsert=True
        )
        return True
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan pengaturan {key}: {e}")
        return False

async def get_setting(key: str, default: Any = None) -> Any:
    """Mengambil pengaturan dari database dengan fallback default."""
    try:
        setting = await settings_collection.find_one({"key": key})
        return setting["value"] if setting else default
    except Exception as e:
        print(f"[ERROR] Gagal mengambil pengaturan {key}: {e}")
        return default

# --- Custom Strings Functions ---
async def load_all_custom_strings() -> Dict[str, str]:
    """Memuat semua custom string dari database."""
    try:
        result = await custom_strings_collection.find_one({"_id": "strings"})
        return result.get("data", {}) if result else {}
    except Exception as e:
        print(f"[ERROR] Gagal memuat custom strings: {e}")
        return {}

# --- Blacklist Functions ---
async def add_to_blacklist(chat_id: int, reason: str = "") -> bool:
    """Menambahkan chat ke blacklist gcast."""
    try:
        await blacklist_collection.update_one(
            {"chat_id": chat_id},
            {"$set": {"chat_id": chat_id, "reason": reason, "added_at": datetime.utcnow()}},
            upsert=True
        )
        return True
    except Exception as e:
        print(f"[ERROR] Gagal menambahkan ke blacklist {chat_id}: {e}")
        return False

async def remove_from_blacklist(chat_id: int) -> bool:
    """Menghapus chat dari blacklist gcast."""
    try:
        result = await blacklist_collection.delete_one({"chat_id": chat_id})
        return result.deleted_count > 0
    except Exception as e:
        print(f"[ERROR] Gagal menghapus dari blacklist {chat_id}: {e}")
        return False

async def is_blacklisted(chat_id: int) -> bool:
    """Memeriksa apakah sebuah chat ada di dalam blacklist."""
    try:
        result = await blacklist_collection.find_one({"chat_id": chat_id})
        return result is not None
    except Exception as e:
        print(f"[ERROR] Gagal memeriksa blacklist {chat_id}: {e}")
        return False

async def get_blacklist() -> list:
    """Mengambil semua chat yang ada di blacklist."""
    try:
        cursor = blacklist_collection.find({})
        return [doc async for doc in cursor]
    except Exception as e:
        print(f"[ERROR] Gagal mengambil blacklist: {e}")
        return []

# --- Database Health & Initialization ---
async def initialize_database
