from . import operasi

DB_NAME = "database.txt"
TEMPLATE = {
    "pk":"XXXXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":255*" ",
    "penulis":255*" ",
    "tahun":"yyyy"
}


def init_console():
    
    try:
        with open(DB_NAME,"r") as file:
            print("Database ada coy, init selesai!")
    except:
        print("Database tidak ditemukan coy, Silahkan membuat Database baru")
        operasi.buat_data_pertama()
           