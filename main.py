#main(Skrip Utama Userbot)Ini adalah bagian terpenting. Saya mempertahankan semua kode bagus Anda dan menambahkan bagian yang hilang untuk menangani perintah.import asyncio
import sys
import signal
from pyrogram import Client, idle, filters  # [REVISI] Menambahkan 'filters'
from pyrogram.errors import (
    AuthKeyUnregistered, 
    AuthKeyInvalid, 
    SessionExpired,
    ApiIdInvalid,
    PhoneNumberInvalid
)

# ============================================
# KONFIGURASI MANUAL - GANTI DENGAN DATA ANDA
# ============================================
API_ID = 29919905
API_HASH = "717957f0e3ae20a7db004d08b66bfd30"
SESSION_STRING = "BQHIiqEAObfrXJ8CaKhDVJZgxQfGLY3R0nuR8YVRLj6h7r7Vy8tW0lWeZ-fAmQtJ6_61jRffQ5fl5mhAf_Ou74ONOJ7VkYydFhLgqQlrKSR12XOotiwseR11YAOqOUJMp4OqR2DC0isN3Sv4lh9F2l_2xhzFd1egVI2e-B1ZKf_F_Zm8bXtZT_slHOZOIfXOxJx6CXYrutW5mxaU1AAuV-5DV1TE5JFNR5QM136h4FqHxLvHZrkGsMfb0_p7p5_o-QSxf91gcIkIGlSIgeTYTNN-llfDTRiF9pjXQRCuqKIihvmM7h0M2moBD7pe_05MLhChi871lTTiamzU-EpyKTOIK6y2zAAAAAHTuBoQAA"

# ============================================
# VALIDASI KONFIGURASI (Tidak ada perubahan, sudah bagus)
# ============================================
def validate_config():
    errors = []
    if not API_ID or not isinstance(API_ID, int): errors.append("API_ID tidak valid atau bukan angka.")
    if not API_HASH or len(API_HASH) < 30: errors.append("API_HASH tidak valid.")
    if not SESSION_STRING or len(SESSION_STRING) < 300: errors.append("SESSION_STRING kosong atau tidak valid.")
    return errors

# ============================================
# INISIALISASI CLIENT (Tidak ada perubahan, sudah bagus)
# ============================================
app = Client(
    name="vzoelubot",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION_STRING,
    in_memory=True
)

# ============================================
# [REVISI] BAGIAN BARU: COMMAND HANDLERS
# ============================================
# Di sinilah semua logika dan perintah bot Anda akan ditempatkan.
# Ini adalah alasan kenapa command Anda sebelumnya tidak berjalan.

@app.on_message(filters.command("alive") & filters.me)
async def alive_command(client, message):
    """
    Handler untuk perintah .alive
    - filters.command("alive"): Merespon ke .alive atau /alive
    - & filters.me: DAN HANYA jika pesan itu dikirim oleh Anda sendiri (wajib untuk userbot)
    """
    # Menggunakan message.edit() lebih baik untuk userbot
    await message.edit_text("**Vzoel-UBOT Aktif**.. 🚀")

# Anda bisa menambahkan command lain di bawah sini dengan format yang sama
# @app.on_message(filters.command("nama_perintah") & filters.me)
# async def nama_fungsi_command(client, message):
#     await message.edit_text("Respon dari perintah Anda")

# ============================================
# MAIN FUNCTION (Tidak ada perubahan, sudah bagus)
# ============================================
async def main():
    print("=" * 60)
    print("🤖 VZOELUBOT - TELEGRAM USERBOT")
    print("=" * 60)
    
    config_errors = validate_config()
    if config_errors:
        for error in config_errors: print(f"❌ {error}")
        return
    
    print("✅ Konfigurasi valid!")
    
    try:
        print("🚀 Memulai userbot...")
        await app.start()
        me = await app.get_me()
        print(f"✅ Userbot berhasil dimulai! Logged in as: {me.first_name}")
        print("-" * 60)
        await idle()
        
    except (AuthKeyUnregistered, SessionExpired):
        print("❌ Session string tidak valid atau sudah expired! Buat yang baru dengan client.py")
    except Exception as e:
        print(f"❌ Error tak terduga saat menjalankan bot: {e}")
        
    finally:
        print("\n🛑 Memulai proses shutdown...")
        if app.is_connected:
            await app.stop()
            print("✅ Client berhasil dihentikan.")
        else:
            print("ℹ️  Client sudah terputus.")

# ============================================
# ENTRY POINT (Tidak ada perubahan, sudah bagus)
# ============================================
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("\n🏁 Program selesai.")
        sys.exit(0)
    

