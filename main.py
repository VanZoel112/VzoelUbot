import asyncio
import sys
import signal
from pyrogram import Client, idle
from pyrogram.errors import (
    AuthKeyUnregistered, 
    AuthKeyInvalid, 
    SessionExpired,
    ApiIdInvalid,
    PhoneNumberInvalid
)

# ============================================
# KONFIGURASI - GANTI DENGAN DATA ANDA
# ============================================
API_ID = 12345  # Ganti dengan API ID Anda
API_HASH = "your_api_hash"  # Ganti dengan API HASH Anda
SESSION_STRING = "your_session_string"  # Ganti dengan session string dari client.py

# ============================================
# VALIDASI KONFIGURASI
# ============================================
def validate_config():
    """Validasi konfigurasi sebelum memulai bot"""
    errors = []
    
    if API_ID == 12345:
        errors.append("API_ID belum diganti dari nilai default")
    
    if API_HASH == "your_api_hash":
        errors.append("API_HASH belum diganti dari nilai default")
        
    if SESSION_STRING == "your_session_string":
        errors.append("SESSION_STRING belum diganti dari nilai default")
    
    if not SESSION_STRING or len(SESSION_STRING) < 300:
        errors.append("SESSION_STRING tidak valid (terlalu pendek)")
    
    return errors

# ============================================
# INISIALISASI CLIENT
# ============================================
def create_client():
    """Membuat instance client Pyrogram"""
    try:
        return Client(
            name="vzoelubot",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION_STRING,
            in_memory=True  # Tidak menyimpan session ke file
        )
    except Exception as e:
        print(f"❌ Error membuat client: {e}")
        return None

# ============================================
# SIGNAL HANDLER
# ============================================
def signal_handler(signum, frame):
    """Handler untuk menangani sinyal sistem"""
    print(f"\n⚠️  Menerima sinyal {signum}. Memulai shutdown...")
    # asyncio.current_task akan menangani cleanup di main()

# ============================================
# MAIN FUNCTION
# ============================================
async def main():
    """Fungsi utama untuk menjalankan userbot"""
    
    # Banner
    print("=" * 60)
    print("🤖 VZOELUBOT - TELEGRAM USERBOT")
    print("=" * 60)
    
    # Validasi konfigurasi
    print("🔍 Memvalidasi konfigurasi...")
    config_errors = validate_config()
    
    if config_errors:
        print("\n❌ KESALAHAN KONFIGURASI:")
        for error in config_errors:
            print(f"   • {error}")
        print("\n💡 Solusi:")
        print("   1. Jalankan client.py untuk mendapatkan session string")
        print("   2. Ganti nilai API_ID, API_HASH, dan SESSION_STRING di main.py")
        return
    
    print("✅ Konfigurasi valid!")
    
    # Membuat client
    print("🔄 Membuat client Pyrogram...")
    app = create_client()
    
    if not app:
        print("❌ Gagal membuat client!")
        return
    
    try:
        print("🚀 Memulai userbot...")
        await app.start()
        
        # Mendapatkan info user
        me = await app.get_me()
        print(f"✅ Userbot berhasil dimulai!")
        print(f"👤 Logged in as: {me.first_name}")
        print(f"📱 Phone: {me.phone_number}")
        print(f"🆔 User ID: {me.id}")
        
        print("\n🎯 Bot sedang berjalan. Tekan Ctrl+C untuk menghentikan...")
        print("-" * 60)
        
        # Menjalankan bot (idle sampai dihentikan)
        await idle()
        
    except AuthKeyUnregistered:
        print("❌ Session string tidak valid atau sudah expired!")
        print("💡 Jalankan client.py untuk membuat session string baru.")
        
    except AuthKeyInvalid:
        print("❌ Session string tidak valid!")
        print("💡 Pastikan session string yang Anda gunakan benar.")
        
    except SessionExpired:
        print("❌ Session sudah expired!")
        print("💡 Jalankan client.py untuk membuat session string baru.")
        
    except ApiIdInvalid:
        print("❌ API ID tidak valid!")
        print("💡 Periksa kembali API_ID di konfigurasi.")
        
    except PhoneNumberInvalid:
        print("❌ Nomor telepon tidak valid!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Keyboard interrupt diterima...")
        
    except Exception as e:
        print(f"❌ Error tak terduga: {e}")
        print(f"📝 Error type: {type(e).__name__}")
        
    finally:
        print("\n🛑 Memulai proses shutdown...")
        
        # Cek apakah client masih terhubung
        try:
            if app.is_connected:
                print("🔄 Menghentikan client...")
                await app.stop()
                print("✅ Client berhasil dihentikan.")
            else:
                print("ℹ️  Client sudah terputus.")
        except Exception as e:
            print(f"⚠️  Error saat menghentikan client: {e}")
        
        print("👋 Userbot telah dihentikan. Terima kasih!")

# ============================================
# ENTRY POINT
# ============================================
if __name__ == "__main__":
    # Setup signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        # Jalankan main function
        asyncio.run(main())
        
    except KeyboardInterrupt:
        print("\n👋 Program dihentikan oleh user.")
        
    except Exception as e:
        print(f"\n❌ Error di level tertinggi: {e}")
        sys.exit(1)
        
    finally:
        print("\n🏁 Program selesai.")
        sys.exit(0)
