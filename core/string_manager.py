# core/string_manager.py
import json
from pathlib import Path
from typing import Any

STRINGS = {}
STRINGS_PATH = Path("assets/messages/")

def load_strings():
    """Memuat semua file .json dari folder assets/messages/."""
    global STRINGS
    if not STRINGS_PATH.is_dir():
        print("[WARNING] Folder assets/messages/ tidak ditemukan. Tidak ada string kustom yang dimuat.")
        return

    for file in STRINGS_PATH.glob("*.json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                STRINGS.update(json.load(f))
        except (json.JSONDecodeError, IOError) as e:
            print(f"[ERROR] Gagal memuat file string {file.name}: {e}")
    
    print(f"[INFO] Berhasil memuat {len(STRINGS)} kunci string dari aset.")

def get_string(key: str) -> Any:
    """Mengambil string atau list dari memori."""
    # Menggunakan format KEY.SUBKEY untuk akses mudah
    keys = key.upper().split('.')
    value = STRINGS
    for k in keys:
        if isinstance(value, dict):
            value = value.get(k)
        else:
            return None # Key tidak valid
    return value
