import asyncio
from pyrogram import Client
import sys

async def main():
    print("=== TELEGRAM SESSION STRING GENERATOR ===\n")
    
    try:
        api_id = int(input("29919905 "))
        api_hash = input("717957f0e3ae20a7db004d08b66bfd30 ").strip()
        
        if not api_hash:
            print("API HASH tidak boleh kosong!")
            return
            
    except ValueError:
        print("Error: API ID harus berupa angka.")
        return
    except KeyboardInterrupt:
        print("\nProses dibatalkan oleh user.")
        return

    print("\n🔄 Membuat koneksi ke Telegram...")
    
    try:
        # Menggunakan session sementara
        async with Client("temp_session", api_id=api_id, api_hash=api_hash) as app:
            print("✅ Koneksi berhasil!")
            print("\n📱 Proses otentikasi akan dimulai...")
            print("   - Masukkan nomor telepon dengan kode negara (contoh: +6281234567890)")
            print("   - Masukkan kode verifikasi yang dikirim ke Telegram")
            print("   - Jika ada 2FA, masukkan password Anda")
            
            # Export session string
            session_string = await app.export_session_string()
            
            print("\n" + "="*70)
            print("🎉 BERHASIL! SESSION STRING TELAH DIBUAT")
            print("="*70)
            print("\n📋 Session String Anda:")
            print("-" * 50)
            print(session_string)
            print("-" * 50)
            
            print("\n⚠️  PENTING:")
            print("   • Simpan session string ini dengan aman")
            print("   • Jangan bagikan kepada siapapun")
            print("   • Gunakan session string ini di main.py")
            
            print(f"\n💾 Session string juga disimpan ke file: session_string.txt")
            
            # Simpan ke file
            with open("session_string.txt", "w") as f:
                f.write(session_string)
            
    except Exception as e:
        print(f"\n❌ Error saat membuat session: {e}")
        print("\nKemungkinan penyebab:")
        print("   • API ID atau API HASH salah")
        print("   • Koneksi internet bermasalah")
        print("   • Server Telegram sedang maintenance")
        
    finally:
        # Hapus file session sementara jika ada
        try:
            import os
            if os.path.exists("temp_session.session"):
                os.remove("temp_session.session")
        except:
            pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh user.")
    except Exception as e:
        print(f"\n❌ Error tak terduga: {e}")
        sys.exit(1)