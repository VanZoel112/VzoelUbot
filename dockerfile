# VzoelUbotversi69 #byVzoelFox's #©2025 ~ Vzoel (Lutpan)

# --- Tahap 1: Base Image ---
# Memulai dari image Python resmi yang ringan (slim) berbasis Debian Bullseye.
# Ini menyediakan lingkungan Python yang stabil tanpa "lemak" yang tidak perlu.
FROM python:3.11-slim-bullseye

# --- Tahap 2: Konfigurasi Lingkungan ---
# Menetapkan direktori kerja di dalam container. Semua perintah selanjutnya akan dijalankan dari sini.
WORKDIR /app

# Mengatur variabel lingkungan agar Python tidak membuat file .pyc dan outputnya langsung tampil.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- Tahap 3: Instalasi Dependencies ---
# Menyalin HANYA file requirements.txt terlebih dahulu.
# Ini adalah langkah optimalisasi. Docker akan menyimpan layer ini dalam cache.
# Jika Anda mengubah kode aplikasi tapi tidak mengubah dependencies, proses build akan jauh lebih cepat.
COPY requirements.txt .

# Menjalankan perintah pip untuk menginstal semua pustaka yang dibutuhkan.
# --no-cache-dir mengurangi ukuran image akhir.
RUN pip install --no-cache-dir -r requirements.txt

# --- Tahap 4: Menyalin Kode Aplikasi ---
# Setelah dependencies terinstal, baru salin seluruh kode proyek Anda.
# Titik pertama (.) berarti menyalin semua dari direktori saat ini (di komputer Anda).
# Titik kedua (.) berarti menyalin ke direktori kerja saat ini di dalam container (/app).
COPY . .

# --- Tahap 5: Perintah Eksekusi ---
# Menetapkan perintah default yang akan dijalankan saat container dimulai.
# Ini akan menjalankan file utama Anda menggunakan Python.
CMD ["python", "main.py"]
