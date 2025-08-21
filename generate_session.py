# generate_session.py (Versi Diagnostik)

import logging
from pyrogram import Client

# Mengatur logging untuk merekam semua detail ke file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("session_generator.log"),
        logging.StreamHandler() # Juga menampilkan log ke terminal
    ]
)

LOGGER = logging.getLogger(__name__)
LOGGER.info("Memulai proses pembuatan string sesi dengan logging detail...")

# --- Mulai Proses ---
try:
    print("\nAnda akan diminta untuk memasukkan API ID & Hash.")
    api_id = int(input("Masukkan API ID: "))
    api_hash = input("Masukkan API Hash: ")

    # Menggunakan "in_memory=True" agar tidak membuat file .session
    with Client(name="session_generator", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
        session_string = app.export_session_string()
        
        print("\n\n" + "="*50)
        print("!!! BERHASIL !!! SIMPAN STRING SESI INI DENGAN SANGAT AMAN !!!")
        print("="*50 + "\n")
        print(session_string)
        print("\n" + "="*50)
        LOGGER.info("String sesi berhasil dibuat dan ditampilkan.")

except Exception as e:
    LOGGER.error(f"Terjadi error yang tidak terduga: {e}", exc_info=True)
    print("\n\n" + "="*50)
    print("!!! PROSES GAGAL !!!")
    print("Sebuah error terjadi. Silakan periksa file 'session_generator.log' untuk detail teknis.")
    print("="*50)
