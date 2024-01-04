
def init_console():
    try:
        with open("data.txt", "r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silakan membuat database baru")
        with open("data.txt", "w", encoding="utf-8") as file:
            penulis = input("Penulis: ")
            judul = input("Judul: ")
            tahun = input("Tahun: ")
            data_str = f"{penulis}, {judul}, {tahun}"
            file.write(data_str)