from model.daftar_nilai import *
from view.view_nilai import cetak_daftar_nilai
from view.input_nilai import input_data


while True:
    pilihan = input("\n[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar] :")
    if pilihan == "T":
        print("\nTambah Data")
        input_data()
    elif pilihan == "L":
        cetak_daftar_nilai()
    elif pilihan == "U":
        ubah_data()
    elif pilihan == "H":
        hapus_data()
    elif pilihan == "C":
        cari_data()
    elif pilihan == "K":
        exit()
    else:
        print("gunakan hanya kata kunci diatas!! (Huruf Kapital)")
