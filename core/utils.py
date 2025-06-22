def input_pilihan(message: str, pilihanArr: tuple):
    while True:
        pilihan = input_int(message)

        if pilihan in pilihanArr: return pilihan


def input_int(message: str):
    while True:
        pilihan = input(message)
        try: 
            pilihan = int(pilihan)
            return pilihan
        except: 
            print("Input harus berupa angka!")
            continue
