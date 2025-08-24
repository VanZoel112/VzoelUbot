import asyncio
import sys
import signal
import traceback
from pyrogram import Client, idle
from pyrogram.errors import (
    AuthKeyUnregistered, 
    AuthKeyInvalid, 
    SessionExpired,
    ApiIdInvalid,
    PhoneNumberInvalid,
    FloodWait
)

# ============================================
# KONFIGURASI MANUAL - GANTI DENGAN DATA ANDA
# ============================================
API_ID = 29919905  # GANTI DISINI dengan API ID Anda
API_HASH = "717957f0e3ae20a7db004d08b66bfd30"  # GANTI DISINI dengan API HASH Anda
SESSION_STRING = "BQHIiqEAOKSDyIjv1Kuc6GSdVJlamdVLp6yCCEcyebPZ6lEondK0eBXGpvEQ0f1Pde74ALDbwqSSrYOoPQqKgbFsUO1wAk0EtevFAACsfZFduVbDKygA9JNs8PbpL9vk7swrPBqRMLUMwSF2rBodXQ-EPHW101GpPZVGqWw7wBA6O6ZgMeXXGoXRKRTfwor0AorgBvMbkBkPxdM_FKqYyp6IB3IEcKI8NAFd4uat64XW2T_SonWiztn-0lvBVuyc6LGHqLyUjFpfb7hqQ-vPwoHkQ9IK-8pNTR6AVX79nP-WOCL6QN-p6A76xyu_bid8fIZH_l0a8"  # ISI dengan session string dari client.py

# ============================================
# DEBUG FUNCTIONS
# ============================================
def debug_session_string(session_string):
    """Debug session string untuk melihat apakah valid"""
    if not session_string:
        return "❌ Session string kosong"
    
    if len(session_string) < 300:
        return f"❌ Session string terlalu pendek ({len(session_string)} karakter, minimal 300)"
    
    if not session_string.startswith("1"):
        return f"❌ Session string tidak dimulai dengan '1' (dimulai dengan: '{session_string[:10]}')"
    
    # Cek apakah mengandung karakter yang valid untuk base64
    import string
    valid_chars = string.ascii_letters + string.digits + "+/="
    invalid_chars = [c for c in session_string if c not in valid_chars]
    if invalid_chars:
        return f"❌ Session string mengandung karakter tidak valid: {set(invalid_chars)}"
    
    return f"✅ Session string tampak valid ({len(session_string)} karakter)"

def validate_config_detailed():
    """Validasi konfigurasi dengan detail lebih lengkap"""
    print("🔍 VALIDASI KONFIGURASI DETAIL:")
    print("-" * 50)
    
    # Check API_ID
    print(f"📋 API_ID: {API_ID}")
    if API_ID == 12345:
        print("   ❌ Masih menggunakan nilai default!")
        return False
    elif not isinstance(API_ID, int):
        print("   ❌ Harus berupa integer!")
        return False
    elif API_ID <= 0:
        print("   ❌ Harus lebih besar dari 0!")
        return False
    else:
        print("   ✅ Valid")
    
    # Check API_HASH
    print(f"📋 API_HASH: {API_HASH}")
    if API_HASH == "your_api_hash_here":
        print("   ❌ Masih menggunakan nilai default!")
        return False
    elif len(API_HASH) != 32:
        print(f"   ❌ Panjang tidak sesuai ({len(API_HASH)}, seharusnya 32)!")
        return False
    else:
        print("   ✅ Valid")
    
    # Check SESSION_STRING
    print(f"📋 SESSION_STRING: {SESSION_STRING[:50]}{'...' if len(SESSION_STRING) > 50 else ''}")
    session_check = debug_session_string(SESSION_STRING)
    print(f"   {session_check}")
    
    if "❌" in session_check:
        return False
    
    print("-" * 50)
    return True

# ============================================
# MAIN FUNCTION WITH DETAILED ERROR HANDLING
# ============================================
async def main():
    """Fungsi utama dengan error handling detail"""
    
    print("=" * 70)
    print("🤖 VZOELUBOT - DEBUG MODE")
    print("=" * 70)
    
    # Validasi konfigurasi detail
    if not validate_config_detailed():
        print("\n❌ KONFIGURASI TIDAK VALID!")
        print("\n💡 LANGKAH PERBAIKAN:")
        print("1. Pastikan API_ID sudah diisi dengan angka yang benar")
        print("2. Pastikan API_HASH sudah diisi (32 karakter)")
        print("3. Pastikan SESSION_STRING sudah diisi dari client.py")
        print("\n🔧 Contoh konfigurasi yang benar:")
        print("   API_ID = 29919905")
        print('   API_HASH = "717957f0e3ae20a7db004d08b66bfd30"')
        print('   SESSION_STRING = "BQHIiqEAOKSDyIjv1Kuc6GSdVJlamdVLp6yCCEcyebPZ6lEondK0eBXGpvEQ0f1Pde74ALDbwqSSrYOoPQqKgbFsUO1wAk0EtevFAACsfZFduVbDKygA9JNs8PbpL9vk7swrPBqRMLUMwSF2rBodXQ-EPHW101GpPZVGqWw7wBA6O6ZgMeXXGoXRKRTfwor0AorgBvMbkBkPxdM_FKqYyp6IB3IEcKI8NAFd4uat64XW2T_SonWiztn-0lvBVuyc6LGHqLyUjFpfb7hqQ-vPwoHkQ9IK-8pNTR6AVX79nP-WOCL6QN-p6A76xyu_bid8fIZH_l0a8"')
        return
    
    print("✅ Semua konfigurasi valid!")
    
    # Test membuat client tanpa memulainya
    print("\n🔧 Testing client creation...")
    try:
        app = Client(
            name="vzoelubot_debug",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=SESSION_STRING,
            in_memory=True,
            test_mode=False  # Pastikan tidak dalam test mode
        )
        print("✅ Client berhasil dibuat!")
    except Exception as e:
        print(f"❌ Error saat membuat client: {e}")
        print(f"📝 Error type: {type(e).__name__}")
        print(f"📍 Traceback: {traceback.format_exc()}")
        return
    
    # Coba start client dengan error handling detail
    print("\n🚀 Memulai client...")
    try:
        await app.start()
        print("✅ Client berhasil dimulai!")
        
        # Test basic functionality
        print("🔍 Testing basic functionality...")
        me = await app.get_me()
        
        print(f"\n🎉 BERHASIL TERHUBUNG!")
        print(f"👤 Name: {me.first_name} {me.last_name or ''}")
        print(f"🆔 ID: {me.id}")
        print(f"📱 Phone: {me.phone_number}")
        if me.username:
            print(f"👨‍💼 Username: @{me.username}")
        
        print(f"\n🌟 Userbot siap digunakan!")
        print("⏸️  Tekan Ctrl+C untuk menghentikan...")
        print("-" * 70)
        
        # Keep running
        await idle()
        
    except AuthKeyUnregistered:
        print("❌ AUTH KEY ERROR: Session tidak terdaftar!")
        print("💡 Solusi: Buat session baru dengan client.py")
        
    except AuthKeyInvalid:
        print("❌ AUTH KEY ERROR: Session tidak valid!")
        print("💡 Solusi: Pastikan session string benar dan lengkap")
        
    except SessionExpired:
        print("❌ SESSION ERROR: Session sudah expired!")
        print("💡 Solusi: Buat session baru dengan client.py")
        
    except ApiIdInvalid:
        print("❌ API ERROR: API ID tidak valid!")
        print("💡 Solusi: Periksa API_ID di my.telegram.org")
        
    except FloodWait as e:
        print(f"❌ FLOOD WAIT: Tunggu {e.value} detik sebelum mencoba lagi")
        
    except ConnectionError as e:
        print(f"❌ CONNECTION ERROR: {e}")
        print("💡 Solusi: Periksa koneksi internet")
        
    except Exception as e:
        error_msg = str(e)
        print(f"❌ UNEXPECTED ERROR: {error_msg}")
        print(f"📝 Error type: {type(e).__name__}")
        
        # Analisis error spesifik
        if "unpack requires a buffer" in error_msg:
            print("\n🔍 ANALISIS ERROR 'unpack requires a buffer':")
            print("   • Session string mungkin rusak atau tidak lengkap")
            print("   • API_ID dan API_HASH tidak cocok dengan session")
            print("   • Format session string tidak valid")
            print("\n💡 SOLUSI:")
            print("   1. Hapus session string lama")
            print("   2. Jalankan client.py untuk buat session baru")
            print("   3. Pastikan API_ID dan API_HASH sama persis")
            print("   4. Copy-paste session string dengan hati-hati")
            
        elif "invalid session" in error_msg.lower():
            print("\n💡 SOLUSI: Session tidak valid, buat session baru")
            
        elif "network" in error_msg.lower():
            print("\n💡 SOLUSI: Periksa koneksi internet")
        
        print(f"\n📍 Full traceback:\n{traceback.format_exc()}")
        
    finally:
        print("\n🛑 Cleanup process...")
        try:
            if 'app' in locals() and hasattr(app, 'is_connected') and app.is_connected:
                print("🔄 Stopping client...")
                await app.stop()
                print("✅ Client stopped successfully")
            else:
                print("ℹ️  Client already disconnected")
        except Exception as cleanup_error:
            print(f"⚠️  Cleanup error: {cleanup_error}")
        
        print("👋 Program finished!")

# ============================================
# ENTRY POINT
# ============================================
if __name__ == "__main__":
    try:
        print("🔧 Starting in debug mode...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Top-level error: {e}")
        print(f"📍 Traceback: {traceback.format_exc()}")

        sys.exit(1)

