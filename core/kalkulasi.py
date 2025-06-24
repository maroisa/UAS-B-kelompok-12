import time
from rich.console import Console

from core import utils
from classes.kue_kering.kue_kering import KueKering
from interfaces.pengembangan import Pengembangan

console = Console()

# Kalkulator
def input_produk(produk):
    jumlah = utils.input_int("Masukkan jumlah produk (pcs)")
    profit = hitung_profit(produk)
    console.print(
        "[#87CEFA]Biaya Produksi:[/#87CEFA]", 
        format_rupiah(produk.biaya_produksi), highlight=False
    )
    console.print(
        "[#87CEFA]Harga Jual:[/#87CEFA]", format_rupiah(produk.harga_jual), 
        highlight=False
    )
    console.print(
        "[#87CEFA]Profit:[/#87CEFA]", format_rupiah(profit), 
        highlight=False
    )
    console.print(
        f"[#87CEFA]Total profit ({jumlah} pcs):[/#87CEFA]", 
        format_rupiah(profit * jumlah), highlight=False
    )

    time.sleep(2)

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

def format_rupiah(angka):
    return f"Rp{int(angka):,}".replace(",", ".")