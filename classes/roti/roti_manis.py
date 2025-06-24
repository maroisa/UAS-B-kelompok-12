from classes.roti.roti import Roti
from interfaces.pengembangan import Pengembangan
import time
class RotiManis(Roti, Pengembangan):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Menyiapkan bahan")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Mencampurkan bahan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Menguleni adonan hingga kalis elastis")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()

    def pemanggangan(self):
        print("Memanaskan oven hingga suhu 170–180°C")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Memanggang roti manis hingga matang dan berwarna cokelat keemasan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Mengangkat dan mendinginkan roti manis.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()

    def pengembangan(self):
        print("Mengistirahatkan adonan")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Mengempiskan adonan, lalu membentuknya sesuai selera")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()
        print("Memfermentasikan adonan setelah dibentuk")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(0.5)
            print('.', end='', flush=True)
        print()

    def tampilkan_produk(self):
        print(f"Kode Produk: {self.kode}")
        print(f"Nama Produk: {self.nama}")
        print("Bahan Baku:")
        for b in self.daftar_bahan_baku:
            print(f"  - {b}")
        print(f"Biaya Produksi: Rp{self.biaya_produksi} per pcs")
        print(f"Harga Jual: Rp{self.harga_jual} per pcs")