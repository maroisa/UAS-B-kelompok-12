from core.utils import format_rupiah

from classes.kue_kering.kue_kering import KueKering
from interfaces.pengembangan import Pengembangan
import time
class Muffin(KueKering, Pengembangan):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Menyiapkan bahan")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()
        print("Mencampur bahan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()

    def pemanggangan(self):
        print("Memanaskan oven hingga suhu 175–190°C.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()
        print("Menuangkan adonan ke dalam cup muffin")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()
        print("Memanggang muffin sampai bagian atas mengembang dan matang")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()
        print("Mengeluarkan muffin dari oven mendinginkannya di rak kawat")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()

    def pengembangan(self):
        print("lanjut ke proses pemanggangan karena muffin mengembang cepat ketika di panggang.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()

    def topping(self):
        print("mendinginkan muffin di rak kawat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()
        print("Menyiapkan topping")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()
        print("Memberikan hiasan dengan topping")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(1)
            print('.', end='', flush=True)
        print()

    def tampilkan_produk(self):
        print(f"Kode Produk: {self.kode}")
        print(f"Nama Produk: {self.nama}")
        print("Bahan Baku:")
        for b in self.daftar_bahan_baku:
            print(f"  - {b}")
        print(f"Biaya Produksi: {format_rupiah(self.biaya_produksi)} per pcs")
        print(f"Harga Jual: {format_rupiah(self.harga_jual)} per pcs")