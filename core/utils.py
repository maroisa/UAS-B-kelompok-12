def input_pilihan(message: str, pilihanArr: tuple):
    while True:
        pilihan = input_int(message)
        if pilihan in pilihanArr: return pilihan
        else:
            print(f"Pilihan tidak valid. Harap masukkan salah satu dari {pilihanArr}.")


def input_int(message: str):
    while True:
        nilai = input(message)
        try: 
            nilai = int(nilai)
            if nilai < 0:
                print("Input tidak boleh negatif!")
                continue
            return nilai
        except: 
            print("Input harus berupa angka!")
            continue
