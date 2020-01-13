nim = []
nama = []
tugas = []
uts = []
nakhir = []
uas = []


def input_data():
    masnim = input("NIM\t\t\t : ")
    nim.append({'nim': masnim})
    masnama = input("NAMA\t\t : ")
    nama.append({'nama': masnama})
    masuts = int(input("Nilai UTS\t : "))
    uts.append({'uts': masuts})
    masuas = int(input("Nilai UAS\t : "))
    uas.append({'uas': masuas})
    mastugas = int(input("Nilai Tugas\t : "))
    tugas.append({'tugas': mastugas})
    akhir = (30 * mastugas / 100) + (35 * masuts / 100) + (35 * masuas / 100)
    nakhir.append({'nakhir': akhir})

    tambah_data(nim. )