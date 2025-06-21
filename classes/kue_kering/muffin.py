from classes.kue_kering.kue_kering import KueKering
from interfaces.pengembangan import Pengembangan
import time
class Muffin(KueKering, Pengembangan):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Mencampur bahan kering seperti tepung terigu, baking powder, garam, gula.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mencampur bahan basah seperti telur, susu, minyak/cairan lemak, vanila.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Menyatukan bahan kering dan basah dan mengaduknya secara perlahan sampai tercampur")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def pemanggangan(self):
        print("Memanaskan oven hingga suhu 175–190°C.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Menuangkan adonan ke dalam cup muffin")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Memanggang muffin sampai bagian atas mengembang dan matang")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mengeluarkan muffin dari oven mendinginkannya di rak kawat")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def pengembangan(self):
        print("lanjut ke proses pemanggangan karena muffin menggunakan baking powder sebagai pengembang cepat.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def tampilkan_produk(self):
        print(f"Kode Produk: {self.kode}")
        print(f"Nama Produk: {self.nama}")
        print("Bahan Baku:")
        for b in self.daftar_bahan_baku:
            print(f"  - {b}")
        print(f"Biaya Produksi: Rp{self.biaya_produksi}")
        print(f"Harga Jual: Rp{self.harga_jual}")