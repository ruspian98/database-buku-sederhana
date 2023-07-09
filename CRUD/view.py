from . import operasi

#HAPUS DATA
def hapus_console():
    read_console()
    while(True):
        print("Pilih Data Yang Akan Dihapus")
        no_buku = int(input("Pilih Nomor : "))
        data_buku = operasi.read(index=no_buku)
        if data_buku:

            # DATA BREAK
            data_break = data_buku.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # DATA YANG AKAN DIHAPUS
            print("_"*100,"\n")
            print("Pilih Data Yang Akan Dihapus")
            print("_"*100)
            print(f"1. Judul Buku : {judul:40}")
            print(f"2. Penulis Buku : {penulis:40}")
            print(f"3. Tahun Terbit : {tahun:4}")

            sudah = input("Yakin Coy? (y/n) : ")
            if sudah == "y" or sudah == "Y":
                operasi.hapus(no_buku)
                break

        else:
            print("Waduh Gak Ada Coy, Coba Lagi Deh ")

    print("data berhasil dihapus")
        

# UPDATE DATA
def update_console():
    read_console()
    
    while(True):
        print("Pilih Nomer Buku Yang Akan Diupdate")
        no_buku = int(input("Nomor Buku : "))
        data_buku = operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("Waduh Gak Ada Coy, Coba Lagi Deh ")

    data_break = data_buku.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # DATA YANG MAU DIUPDATE
        print("_"*100,"\n")
        print("Pilih Data Yang Akan Diubah")
        print("_"*100)
        print(f"1. Judul Buku : {judul:40}")
        print(f"2. Penulis Buku : {penulis:40}")
        print(f"3. Tahun Terbit : {tahun:4}")

        # MEMILIH MODE UNTUK UPDATE
        user_option = input("Pilih Data : ")
        print("_"*100,"\n")

        match user_option:
            case "1": judul = input("Masukkan Judul Yang Baru :")
            case "2": penulis = input("Masukkan Penulis Yang Baru :")
            case "3": 
                while(True):
                    try:
                        tahun = int(input("Tahun Rilis : "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Isi Tahun Dengan Angka Coy, Coba Lagi ")
                    except:
                        print("Isi Tahun Dengan Angka Coy, Coba Lagi ")
            case _: print("Index Yang Anda Masukkan Tidak Cocok")

        print("Data Baru Anda")
        print(f"1. Judul Buku : {judul:40}")
        print(f"2. Penulis Buku : {penulis:40}")
        print(f"3. Tahun Terbit : {tahun:4}")

        sudah = input("Sudah Coy? (y/n) : ")
        if sudah == "y" or sudah == "Y":
            break
    
    operasi.update(no_buku,pk,date_add,penulis,judul,tahun)


# MENAMBAH DATA
def tambah_console():
    print("_"*100,"\n")
    print("Silahkan Tambah Data Buku Baru")
    print("_"*100)
    penulis = input("Penulis Buku : ")
    judul = input("Judul Buku : ")
    while(True):
        try:
            tahun = int(input("Tahun Rilis : "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Isi Tahun Dengan Angka Coy, Coba Lagi ")
        except:
            print("Isi Tahun Dengan Angka Coy, Coba Lagi ")

    operasi.tambah(tahun,judul,penulis)
    print("\nIni Adalah Data Baru Anda")
    read_console()



# MELIHAT DATA
def read_console():
    data_file = operasi.read()
    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"



# HEADER
    print("="*100)
    print(f"{index:4} | {judul:50} | {penulis:30} | {tahun:4}")
    print("_"*100)
    
# DATA
    for index,data in enumerate(data_file):
        data_break = data.split(',')
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.50} | {penulis:.30} | {tahun:4}",end="")



# FOOTER
    print("="*100,"\n")



    
