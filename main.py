import asyncio
from pyrogram import Client, idle

# Asumsikan ini adalah inisialisasi klien Anda
# Ganti dengan detail API_ID, API_HASH, dan SESSION_STRING Anda
app = Client(
    "vzoelubot",
    api_id=12345,
    api_hash="your_api_hash",
    session_string="your_session_string"
)

async def main():
    """
    Fungsi utama untuk memulai, menjalankan, dan menghentikan bot
    dengan penanganan kesalahan yang benar.
    """
    try:
        print("Memulai Userbot...")
        await app.start()
        print("Userbot telah dimulai. Menunggu perintah...")
        
        # Ini akan membuat bot tetap berjalan sampai dihentikan
        await idle()
        
    except (KeyboardInterrupt, SystemExit):
        # Menangkap interupsi dari keyboard (Ctrl+C) atau sinyal keluar sistem
        print("Menerima sinyal shutdown...")
        
    finally:
        print("Memulai proses shutdown Userbot...")
        # Cek terlebih dahulu apakah klien masih terhubung sebelum mencoba menghentikannya
        if app.is_connected:
            print("Menghentikan klien Pyrogram...")
            await app.stop()
            print("Klien berhasil dihentikan.")
        else:
            print("Klien sudah terputus, tidak perlu dihentikan lagi.")

if __name__ == "__main__":
    # Cara standar untuk menjalankan fungsi async
    # Ini akan menangani loop event asyncio secara otomatis
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Terjadi kesalahan tak terduga di level atas: {e}")
