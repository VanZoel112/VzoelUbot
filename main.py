# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

# main.py (Versi Revisi)

import asyncio
from pyrogram import idle
from pytgcalls import PyTgCalls

from core.client import VzoelUbot
from core.database import initialize_database
# ... (sisa impor dan kode main.py Anda)

# Inisialisasi kedua klien
app = VzoelUbot()
pytgcalls_client = PyTgCalls(app)

async def main():
    # ... (fungsi main Anda yang sudah ada)
    try:
        # ...
        await app.start()
        await pytgcalls_client.start() # <-- Jalankan juga klien pytgcalls
        # ...
        await idle()
    finally:
        # ...
        await pytgcalls_client.stop() # <-- Hentikan juga klien pytgcalls
        await app.stop()
        # ...

if __name__ == "__main__":
    asyncio.run(main())
