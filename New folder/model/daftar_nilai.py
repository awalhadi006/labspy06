from view.input_nilai import *


def ubah_data():
    masnim = input("Masukkan NIM yang ingin diubah datanya : ")
    for i in range(len(nim)):
        if masnim == nim[i]['nim']:
            masnimnew = input("NIM\t\t\t : ")
            nim[i]['nim'] = masnimnew
            masnamanew = input("Nama\t\t : ")
            nama[i]['nama'] = masnamanew
            masutsnew = int(input("Nilai UTS\t : "))
            uts[i]['uts'] = masutsnew
            masuasnew = int(input("Nilai UAS\t : "))
            uas[i]['uas'] = masuasnew
            mastugasnew = int(input("Nilai Tugas\t : "))
            tugas[i]['tugas'] = mastugasnew
            akhirnew = (30 * mastugasnew / 100) + (35 * masutsnew / 100) + (35 * masuasnew / 100)
            nakhir[i]['nakhir'] = akhirnew
            break
        print("NIM", masnim, "Tidak Ditemukan")


def hapus_data():
    masnim = input("masukan nim : ")
    for i in range(len(nim)):
        if masnim == nim[i]['nim']:
            print("Data dengan NIM : ", nim[i]['nim'], "Telah Dihapus.")
            del nim[i]
            del nama[i]
            del tugas[i]
            del uts[i]
            del uas[i]
            del nakhir[i]
            break
        print("NIM", masnim, "Tidak Ditemukan")


def cari_data():
    masnim = input("Masukkan NIM yang ingin di cari datanya : ")
    for i in range(len(nim)):
        if masnim == nim[i]['nim']:
            print("\nDaftar Nilai")
            print("======================================================================================")
            print("| No |     NIM     |    NAMA    |    TUGAS    |    UTS    |    UAS    |    AKHIR     |")
            print("======================================================================================")
            print("|", i + +1,
                  " | {0:12s}| {1:11.11s}|{2:^13d}|{3:^11d}|{4:^11d}|{5:^14.2f}|".format(nim[i]['nim'], nama[i]['nama'],
                                                                                         tugas[i]['tugas'],
                                                                                         uts[i]['uts'],
                                                                                         uas[i]['uas'],
                                                                                         nakhir[i]['nakhir']))
            print("======================================================================================")
