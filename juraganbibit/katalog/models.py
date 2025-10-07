from django.db import models

class Produk (models.Model):

    nama_bibit = models.CharField(max_length=200, help_text="Contoh: Bibit Lele Mutiara")
    slug = models.SlugField(max_length=255, unique=True, help_text="Otomatis terisi, jangan diubah manual")
    deskripsi_singkat = models.CharField(max_length=255, help_text="Teks singkat untuk halaman katalog")
    deskripsi_lengkap = models.TextField()


    harga = models.CharField(max_length=100, help_text="Contoh: Mulai dari Rp 500/ekor")
    ukuran = models.CharField(max_length=100, help_text="Contoh: 5-7 cm")
    stok_status = models.CharField(max_length=50, choices=[
        ('Tersedia', 'Tersedia'),
        ('Terbatas', 'Terbatas'),
        ('Habis', 'Habis')
    ], default='Tersedia')

    gambar_utama = models.ImageField(upload_to='produk_images/')
    is_unggulan = models.BooleanField(default=False, help_text="Centang untuk menampilkan di homepage")

    dibuat_pada = models.DateTimeField(auto_now_add=True)
    diperbarui_pada = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Produk Bibit"
        verbose_name_plural = "Produk Bibit"

    def __str__(self):
        return self.nama_bibit