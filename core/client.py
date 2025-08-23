import asyncio
from pyrogram import Client

async def main():
    try:
        api_id = int(input("Masukkan API ID Anda: "))
        api_hash = input("Masukkan API HASH Anda: ")
    except ValueError:
        print("API ID harus berupa angka.")
        return

    # Menggunakan ":memory:" berarti sesi tidak akan disimpan sebagai file
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print("\nSilakan masukkan nomor telepon, kode, dan kata sandi Anda...")
        
        session_string = await app.export_session_string()
        
        print("\n================================================================")
        print("         BERHASIL! Salin string sesi di bawah ini:")
        print("================================================================")
        print(session_string)
        print("\n")

if __name__ == "__main__":
    asyncio.run(main())
