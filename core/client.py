import asyncio
import sys
import os
import traceback
from pyrogram import Client

async def main():
    print("=" * 70)
    print("🔧 TELEGRAM SESSION STRING GENERATOR - DEBUG MODE")
    print("=" * 70)
    
    # ============================================
    # ISI MANUAL DISINI - GANTI DENGAN DATA ANDA
    # ============================================
    api_id = 29919905  # GANTI dengan API ID Anda
    api_hash = "717957f0e3ae20a7db004d08b66bfd30"  # GANTI dengan API HASH Anda
    
    # Validasi input
    print("🔍 Validating configuration...")
    print(f"📋 API_ID: {api_id}")
    print(f"📋 API_HASH: {api_hash}")
    
    if api_id == 12345:
        print("❌ Error: API_ID masih menggunakan nilai default!")
        print("💡 Edit file ini dan ganti api_id = 12345 dengan ID asli Anda")
        print("🌐 Dapatkan di: https://my.telegram.org/apps")
        return
        
    if api_hash == "your_api_hash_here":
        print("❌ Error: API_HASH masih menggunakan nilai default!")
        print("💡 Edit file ini dan ganti api_hash dengan hash asli Anda")
        print("🌐 Dapatkan di: https://my.telegram.org/apps")
        return
    
    if not isinstance(api_id, int) or api_id <= 0:
        print("❌ Error: API_ID harus berupa angka positif!")
        return
        
    if len(api_hash) != 32:
        print(f"❌ Error: API_HASH harus 32 karakter! (saat ini: {len(api_hash)})")
        return
    
    print("✅ Konfigurasi valid!")
    print(f"✅ API_ID: {api_id}")
    print(f"✅ API_HASH: {api_hash[:8]}...{api_hash[-4:]}")
    
    print("\n🔄 Creating Pyrogram client...")
    
    # Nama session yang unik untuk menghindari konflik
    session_name = f"temp_session_{api_id}"
    
    try:
        # Buat client dengan konfigurasi yang lebih aman
        app = Client(
            name=session_name,
            api_id=api_id,
            api_hash=api_hash,
            in_memory=False,  # Simpan session sementara ke file
            test_mode=False   # Pastikan tidak dalam test mode
        )
        
        print("✅ Client created successfully!")
        print("\n📱 Starting authentication process...")
        print("=" * 50)
        print("PETUNJUK LOGIN:")
        print("• Masukkan nomor telepon dengan kode negara")
        print("  Contoh: +6281234567890")
        print("• Masukkan kode verifikasi dari Telegram")
        print("• Jika ada 2FA, masukkan password Anda")
        print("=" * 50)
        
        # Mulai client dan proses otentikasi
        await app.start()
        
        print("\n🎉 Authentication successful!")
        print("🔄 Generating session string...")
        
        # Export session string
        session_string = await app.export_session_string()
        
        # Validasi session string yang dihasilkan
        if not session_string:
            print("❌ Error: Session string kosong!")
            return
            
        if len(session_string) < 300:
            print(f"❌ Error: Session string terlalu pendek ({len(session_string)} karakter)")
            return
            
        print("\n" + "="*70)
        print("🎉 SUCCESS! SESSION STRING GENERATED")
        print("="*70)
        
        print(f"\n📊 Session Info:")
        print(f"   Length: {len(session_string)} characters")
        print(f"   Starts with: {session_string[:20]}...")
        print(f"   Ends with: ...{session_string[-20:]}")
        
        print(f"\n📋 YOUR SESSION STRING:")
        print("-" * 50)
        print(session_string)
        print("-" * 50)
        
        # Simpan ke file
        filename = "session_string.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(session_string)
            print(f"\n💾 Session string saved to: {filename}")
        except Exception as save_error:
            print(f"⚠️  Could not save to file: {save_error}")
        
        # Tampilkan informasi user
        try:
            me = await app.get_me()
            print(f"\n👤 Account Info:")
            print(f"   Name: {me.first_name} {me.last_name or ''}")
            print(f"   Phone: {me.phone_number}")
            print(f"   ID: {me.id}")
            if me.username:
                print(f"   Username: @{me.username}")
        except Exception as user_error:
            print(f"⚠️  Could not get user info: {user_error}")
        
        print(f"\n📝 NEXT STEPS:")
        print("1. Copy session string di atas")
        print("2. Buka main.py")
        print("3. Ganti SESSION_STRING dengan session string ini")
        print("4. Pastikan API_ID dan API_HASH di main.py sama dengan di sini")
        print("5. Jalankan: python3 main.py")
        
        print(f"\n⚠️  IMPORTANT:")
        print("• Jangan bagikan session string kepada siapapun!")
        print("• Session string memberikan akses penuh ke akun Anda")
        print("• Simpan session string dengan aman")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Process cancelled by user")
        
    except Exception as e:
        error_msg = str(e)
        print(f"\n❌ ERROR: {error_msg}")
        print(f"📝 Error type: {type(e).__name__}")
        
        # Analisis error spesifik
        if "phone number" in error_msg.lower():
            print("\n💡 PHONE NUMBER ERROR:")
            print("   • Pastikan format nomor benar: +6281234567890")
            print("   • Gunakan kode negara yang sesuai")
            
        elif "invalid code" in error_msg.lower():
            print("\n💡 VERIFICATION CODE ERROR:")
            print("   • Pastikan kode verifikasi benar")
            print("   • Tunggu kode baru jika sudah expired")
            
        elif "api" in error_msg.lower():
            print("\n💡 API ERROR:")
            print("   • Periksa API_ID dan API_HASH di my.telegram.org")
            print("   • Pastikan tidak ada spasi atau karakter tambahan")
            
        elif "flood" in error_msg.lower():
            print("\n💡 FLOOD ERROR:")
            print("   • Terlalu banyak percobaan login")
            print("   • Tunggu beberapa menit sebelum mencoba lagi")
            
        print(f"\n📍 Full error details:")
        print(traceback.format_exc())
        
    finally:
        print("\n🧹 Cleaning up...")
        try:
            # Stop client jika masih berjalan
            if 'app' in locals() and hasattr(app, 'is_connected'):
                if app.is_connected:
                    await app.stop()
                    print("✅ Client stopped")
            
            # Hapus file session sementara
            session_file = f"{session_name}.session"
            if os.path.exists(session_file):
                os.remove(session_file)
                print(f"🗑️  Temporary session file removed: {session_file}")
                
        except Exception as cleanup_error:
            print(f"⚠️  Cleanup error: {cleanup_error}")
        
        print("👋 Session generator finished!")

if __name__ == "__main__":
    try:
        print("🚀 Starting session generator...")
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user")
    except Exception as e:
        print(f"\n❌ Top-level error: {e}")
        print(f"📍 Traceback: {traceback.format_exc()}")
        sys.exit(1)