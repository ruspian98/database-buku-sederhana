'''PERSIAPAN'''
import os
import CRUD as CRUD


if __name__ == "__main__": # KONFENSI RUNNING PROGRAM AGAR LEBIH RAPI
    sistem_operasi = os.name # MENDETEKSI SYSTEM OPERASI

    match sistem_operasi: # match --> cocok atau tidak
            case "posix": os.system("clear")
            case "nt": os.system("cls")
         
    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print("=========================")

    '''CHECK DATABASE'''
    CRUD.init_console() # UNTUK CEK DATABASE

    while(True):
        match sistem_operasi: # match --> mengambil sistem operasi yang cocok
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print("SELAMAT DATANG DI PROGRAM")
        print("DATABASE PERPUSTAKAAN")
        print("=========================")

        print(f"1. Buka Data")
        print(f"2. Tambah Data")
        print(f"3. Update Data")
        print(f"4. Hapus Data\n")

        user_input = input("Pilih Opsi: ")

        print("\n=========================\n")

        match user_input: # MENGAMBIL LAGI INPUT DARI USER
            case "1": CRUD.read_console()
            case "2": CRUD.tambah_console()
            case "3": CRUD.update_console()
            case "4": CRUD.hapus_console()

        print("\n=========================\n")

        sudah = input("Sudah Coy? (y/n) : ")
        if sudah == "y" or sudah == "Y":
            break

    print("TERIMA KASIH")