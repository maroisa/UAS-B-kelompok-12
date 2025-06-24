
from core import utils
from classes.kue_kering.kue_kering import KueKering
from interfaces.pengembangan import Pengembangan

# Kalkulator
def input_produk(produk):
    jumlah = utils.input_int("Masukkan jumlah produk (pcs)")
    profit = hitung_profit(produk)
    print("Biaya Produksi:", produk.biaya_produksi)
    print("Harga Jual:", produk.harga_jual)
    print("Profit:", profit)
    print(f"Total profit ({jumlah} pcs):", profit * jumlah)

def hitung_profit(produk):
    return produk.harga_jual - produk.biaya_produksi

# Simulasi
def simulasi(produk):
    print(f"Melakukan pembuatan {produk.nama}...")
    produk.pengadonan()

    if isinstance(produk, Pengembangan):
        produk.pengembangan()
    
    produk.pemanggangan()
    
    if isinstance(produk, KueKering):
        produk.topping()
    
    print(f"\n\n=== {produk.nama.upper()} SUDAH SIAP DISAJIKAN! ===\n")