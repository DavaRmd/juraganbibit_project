# Juragan Bibit Ikan - Website Katalog

Ini adalah proyek website katalog untuk usaha "Juragan Bibit Ikan", dibangun menggunakan Django dan Tailwind CSS. Tujuan website ini adalah untuk menampilkan produk bibit ikan secara online dan mengarahkan calon pembeli untuk melakukan pemesanan via WhatsApp.

---

##  fitur Utama

* **Admin Panel:** Sistem manajemen konten penuh untuk menambah, mengubah, dan menghapus data produk.
* **Halaman Homepage:** Menampilkan produk-produk yang ditandai sebagai unggulan.
* **Halaman Katalog:** Menampilkan semua produk yang tersedia.
* **Halaman Detail Produk:** Menampilkan informasi lengkap (gambar, deskripsi, harga) untuk setiap produk.
* **Desain Responsif:** Tampilan yang menyesuaikan dengan perangkat desktop maupun mobile menggunakan Tailwind CSS.

---

## Teknologi yang Digunakan

* **Backend:** Python & Django Framework
* **Frontend:** HTML & Tailwind CSS (via Play CDN)
* **Database:** MySQL
* **Version Control:** Git & GitHub

---

## Cara Menjalankan Proyek (Lokal)

1.  **Clone repository ini:**
    ```bash
    git clone [URL_REPOSITORY_ANDA]
    cd juraganbibit_project
    ```

2.  **Buat dan aktifkan virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install semua dependensi:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Catatan: Kita perlu membuat file `requirements.txt` ini nanti)*

4.  **Konfigurasi `.env`:** Buat file `.env` untuk menyimpan konfigurasi database.

5.  **Lakukan migrasi database:**
    ```bash
    python manage.py migrate
    ```

6.  **Buat superuser:**
    ```bash
    python manage.py createsuperuser
    ```
    
7.  **Jalankan server development:**
    ```bash
    python manage.py runserver
    ```