from core import utils

from classes.kue_kering.butter_cookies import ButterCookies
from classes.kue_kering.muffin import Muffin
from classes.roti.croissant import Croissant
from classes.roti.roti_manis import RotiManis

def input_produk():
    print("=== Tambah Produk Roti ===")
    print("1. Roti Manis")
    print("2. Croissant")
    print("3. Butter Cookies")
    print("4. Muffin")

    jawaban = utils.input_pilihan("Pilih jenis produk (1-4): ", (1,2,3,4))
    jumlah = utils.input_int("Jumlah produk (pcs): ")
    