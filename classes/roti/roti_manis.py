from classes.roti.roti import Roti
from interfaces.pengembangan import Pengembangan
import time
class RotiManis(Roti, Pengembangan):
    def __init__(self, kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual):
        super().__init__(kode, nama, daftar_bahan_baku, biaya_produksi, harga_jual)

    def pengadonan(self):
        print("Mencampurkan tepung terigu protein tinggi, gula, ragi instan, dan garam.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("menambahkan susu/susu bubuk + air, telur, dan mentega/margarin.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Menguleni adonan hingga kalis elastis")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def pemanggangan(self):
        print("Memanaskan oven hingga suhu 170–180°C")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mengolesi permukaan roti dengan campuran kuning telur dan susu")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Memanggang roti manis hingga matang dan berwarna cokelat keemasan.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mengangkat dan mendinginkan roti manis, lalu mengoleskan margarin di atasnya agar permukaan lembut dan mengilap.")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)

    def pengembangan(self):
        print("Mengistirahatkan adonan")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Mengempiskan adonan, lalu membentuknya sesuai selera")
        print("Sedang dalam proses", end='', flush=True)
        for _ in range(3):  
            time.sleep(2)
            print('.', end='', flush=True)
        print("Memfermentasikan adonan setelah dibentuk")
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