Revisi Final untuk VzoelUBOTBerikut adalah kode yang telah direvisi untuk client.py dan main.py. Perubahan utama ditandai dengan komentar [REVISI].client.py (Generator Session String)Perubahan di sini bersifat minor, hanya untuk membuatnya lebih jelas dan bersih saat dijalankan.import asyncio
import sys

async def main():
    print("=== TELEGRAM SESSION STRING GENERATOR ===\n")
    
    try:
        # [REVISI] Mengubah prompt input agar lebih jelas
        api_id = int(input("▶️ Masukkan API ID Anda: "))
        api_hash = input("▶️ Masukkan API HASH Anda: ").strip()
        
        if not api_hash:
            print("❌ API HASH tidak boleh kosong!")
            return
            
    except ValueError:
        print("❌ Error: API ID harus berupa angka.")
        return
    except KeyboardInterrupt:
        print("\nProses dibatalkan oleh user.")
        return

    print("\n🔄 Membuat koneksi ke Telegram...")
    
    try:
        # [REVISI] Menggunakan ":memory:" agar tidak membuat file .session sama sekali. Lebih bersih.
        async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
            print("✅ Koneksi berhasil!")
            print("\n📱 Proses otentikasi akan dimulai...")
            print("   - Masukkan nomor telepon dengan kode negara (contoh: +6281234567890)")
            print("   - Masukkan kode verifikasi yang dikirim ke Telegram")
            print("   - Jika ada 2FA, masukkan password Anda")
            
            session_string = await app.export_session_string()
            
            print("\n" + "="*70)
            print("🎉 BERHASIL! SESSION STRING TELAH DIBUAT")
            print("="*70)
            print("\n📋 Session String Anda:")
            print("-" * 50)
            print(session_string)
            print("-" * 50)
            
            print("\n⚠️  PENTING:")
            print("   • Simpan session string ini dengan aman dan jangan bagikan kepada siapapun.")
            print("   • Salin dan tempel (paste) string ini ke variabel SESSION_STRING di file main.py")
            
    except Exception as e:
        print(f"\n❌ Error saat membuat session: {e}")
        
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n👋 Program dihentikan oleh user.")
    except Exception as e:
        print(f"\n❌ Error tak terduga: {e}")
        sys.exit(1)
