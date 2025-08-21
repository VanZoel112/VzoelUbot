# generate_session.py
# Skrip ini hanya untuk menghasilkan string sesi. Jalankan satu kali.

from pyrogram import Client

print("Memulai proses pembuatan string sesi...")
print("Anda akan diminta untuk memasukkan API ID, API Hash, dan nomor telepon.")
print("Telegram akan mengirim kode login, masukkan di sini.")
print("Jika Anda memiliki 2FA, Anda juga akan diminta memasukkan password.")

# Meminta input dari Anda
api_id = int(input("Masukkan API ID: "))
api_hash = input("Masukkan API Hash: ")

# Menggunakan "in_memory=True" agar tidak membuat file .session
with Client(name="session_generator", api_id=api_id, api_hash=api_hash, in_memory=True) as app:
    session_string = app.export_session_string()
    print("\n\n" + "="*50)
    print("!!! SIMPAN STRING SESI INI DENGAN SANGAT AMAN !!!")
    print("JANGAN BAGIKAN KEPADA SIAPAPUN.")
    print("="*50 + "\n")
    print(session_string)
    print("\n" + "="*50)
    print("Salin seluruh string di atas dan masukkan ke file .env Anda.")
