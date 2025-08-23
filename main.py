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
# KONFIGURASI MANUAL - GANTI DENGAN DATA ANDA
# ============================================
API_ID = 29919905  # GANTI DISINI dengan API ID Anda (contoh: 1234567)
API_HASH = "717957f0e3ae20a7db004d08b66bfd30"  # GANTI DISINI dengan API HASH Anda (contoh: "abcd1234efgh5678")
SESSION_STRING = ""  # BIARKAN KOSONG DULU - akan diisi dari client.py

# ============================================
# VALIDASI KONFIGURASI
# ============================================
def validate_config():
    """Validasi konfigurasi sebelum memulai bot"""
    errors = []
    
    if API_ID == 12345:
        errors.append("⚠️  API_ID masih menggunakan nilai default (12345)")
        errors.append("    Ganti dengan API ID asli Anda di baris 13")
    
    if API_HASH == "your_api_hash_here":
        errors.append("⚠️  API_HASH masih menggunakan nilai default")
        errors.append("    Ganti dengan API HASH asli Anda di baris 14")
        
    if not SESSION_STRING or SESSION_STRING == "":
        errors.append("⚠️  SESSION_STRING kosong")
        errors.append("    Jalankan client.py dulu untuk mendapatkan session string")
        errors.append("    Kemudian isi SESSION_STRING di baris 15")
    
    if SESSION_STRING and len(SESSION_STRING) < 300:
        errors.append("⚠️  SESSION_STRING tidak valid (terlalu pendek)")
    
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

# ============================================
# MAIN FUNCTION
# ============================================
async def main():
    """Fungsi utama untuk menjalankan userbot"""
    
    # Banner
    print("=" * 60)
    print("🤖 VZOELUBOT - TELEGRAM USERBOT")
    print("=" * 60)
    
    # Tampilkan konfigurasi saat ini
    print("📋 KONFIGURASI SAAT INI:")
    print(f"   API_ID: {API_ID}")
    print(f"   API_HASH: {'✅ Sudah diisi' if API_HASH != 'your_api_hash_here' else '❌ Belum diisi'}")
    print(f"   SESSION_STRING: {'✅ Sudah diisi' if SESSION_STRING else '❌ Belum diisi'}")
    print("-" * 60)
    
    # Validasi konfigurasi
    print("🔍 Memvalidasi konfigurasi...")
    config_errors = validate_config()
    
    if config_errors:
        print("\n❌ KESALAHAN KONFIGURASI:")
        for error in config_errors:
            print(f"   {error}")
        
        print("\n💡 CARA MEMPERBAIKI:")
        print("   1. Buka file main.py dengan text editor")
        print("   2. Ganti API_ID di baris 13 dengan ID asli Anda")
        print("   3. Ganti API_HASH di baris 14 dengan HASH asli Anda") 
        print("   4. Jika belum punya session string:")
        print("      • Jalankan: python3 client.py")
        print("      • Copy session string yang dihasilkan")
        print("      • Paste di SESSION_STRING baris 15")
        print("   5. Save file dan jalankan ulang: python3 main.py")
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
        if me.last_name:
            print(f"    Full name: {me.first_name} {me.last_name}")
        if me.username:
            print(f"    Username: @{me.username}")
        print(f"📱 Phone: {me.phone_number}")
        print(f"🆔 User ID: {me.id}")
        
        print("\n🎯 Bot sedang berjalan. Tekan Ctrl+C untuk menghentikan...")
        print("-" * 60)
        
        # Menjalankan bot (idle sampai dihentikan)
        await idle()
        
    except AuthKeyUnregistered:
        print("❌ Session string tidak valid atau sudah expired!")
        print("💡 Solusi: Jalankan client.py untuk membuat session string baru.")
        
    except AuthKeyInvalid:
        print("❌ Session string tidak valid!")
        print("💡 Solusi: Pastikan session string yang Anda gunakan benar.")
        
    except SessionExpired:
        print("❌ Session sudah expired!")
        print("💡 Solusi: Jalankan client.py untuk membuat session string baru.")
        
    except ApiIdInvalid:
        print("❌ API ID tidak valid!")
        print("💡 Solusi: Periksa kembali API_ID di konfigurasi (baris 13).")
        
    except PhoneNumberInvalid:
        print("❌ Nomor telepon tidak valid!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Keyboard interrupt diterima...")
        
    except Exception as e:
        print(f"❌ Error tak terduga: {e}")
        print(f"📝 Error type: {type(e).__name__}")
        
        # Tampilkan kemungkinan solusi berdasarkan error
        error_str = str(e).lower()
        if "unpack" in error_str:
            print("\n💡 Kemungkinan penyebab error 'unpack':")
            print("   • Session string rusak atau tidak lengkap")
            print("   • API credentials tidak cocok dengan session")
            print("   • Versi Pyrogram tidak kompatibel")
            print("   • Coba buat session string baru dengan client.py")
        
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