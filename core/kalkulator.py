from core import utils

def input_produk(produk):
    jumlah = utils.input_int("Masukkan jumlah produk (pcs): ")
    profit = hitung_profit(produk)
    print("Biaya Produksi:", produk.biaya_produksi)
    print("Harga Jual:", produk.harga_jual)
    print("Profit:", profit)
    print(f"Total profit ({jumlah} pcs):", profit * jumlah)

def hitung_profit(produk):
    return produk.harga_jual - produk.biaya_produksi