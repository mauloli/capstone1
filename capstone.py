from tabulate import tabulate

def tampilkan_menu():
    print("""
=== Capstone Project: Studi Kasus Data Nilai Siswa ===

Menu Data Nilai Siswa:
1. Tampilkan Data Siswa
2. Input Data Siswa
3. Hapus Data Siswa
4. Ubah Data Siswa
5. Keluar Program
""")
    

def tampilkan_data(siswa):
  headers = ["NIM", "Nama", "Nilai", "Kelas", "Jurusan"]
  table = [[s['nim'], s['nama'], s['nilai'], s['kelas'], s['jurusan']] for s in siswa]
  print("\n📋 Daftar Data Siswa:\n")
  print(tabulate(table, headers=headers, tablefmt="grid"))
  print('\n')

def input_data(siswa):
    while True:
        nim = input("Masukkan NIM (unik): ")

        if any(data['nim'] == nim for data in siswa):
            print("❌ NIM sudah terdaftar.")
            ulang = input("Ingin coba input NIM lain? (y/n): ").lower()
            if ulang != 'y':
                print("\n <====== Kembali ke menu utama.\n")
                return
            continue

        nama = input("Masukkan nama siswa: ")
        nilai = input("Masukkan nilai siswa: ")
        kelas = input("Masukkan nama kelas: ")
        jurusan = input("Masukkan jurusan: ")

        siswa.append({
            'nim': nim,
            'nama': nama,
            'nilai': nilai,
            'kelas': kelas,
            'jurusan': jurusan
        })
        print("\n✅ Data siswa berhasil ditambahkan.\n")
        break


def hapus_data(siswa):
    while True:
        tampilkan_data(siswa)
        nim = input("Masukkan NIM yang ingin dihapus: ")
        for i, data in enumerate(siswa):
            if data['nim'] == nim:
                print("\n📌 Data yang akan dihapus:")
                print(tabulate([[data['nim'], data['nama'], data['nilai'], data['kelas'], data['jurusan']]],
                            headers=["NIM", "Nama", "Nilai", "Kelas", "Jurusan"],
                            tablefmt="grid"))
                konfirmasi = input("Yakin ingin menghapus data ini? (y/n): ").lower()
                if konfirmasi == 'y':
                    del siswa[i]
                    print("🗑️ Data siswa berhasil dihapus.\n")
                else:
                    print("❎ Penghapusan dibatalkan.\n")
                return
        print("❌ NIM tidak ditemukan.")
        ulang = input("Ingin coba masukkan NIM lain? (y/n): ").lower()
        if ulang != 'y':
            print("🔙 Kembali ke menu utama.\n")
            return

def ubah_data(siswa):
    if not siswa:
        print("⚠️ Tidak ada data siswa.\n")
        return

    while True:
        nim = input("Masukkan NIM yang ingin diubah: ")
        for data in siswa:
            if data['nim'] == nim:
                while True:
                    print("\n📌 Data ditemukan:")
                    print(tabulate([[data['nim'], data['nama'], data['nilai'], data['kelas'], data['jurusan']]],headers=["NIM", "Nama", "Nilai", "Kelas", "Jurusan"],tablefmt="grid"))

                    print("""
Pilih data yang ingin diubah:
1. Nama
2. Nilai
3. Kelas
4. Jurusan
5. Batal
""")
                    pilihan = input("Masukkan pilihan (1-5): ")

                    if pilihan == '1':
                        data['nama'] = input("Masukkan nama baru: ")
                        print("✅ Nama berhasil diubah.\n")
                    elif pilihan == '2':
                        data['nilai'] = input("Masukkan nilai baru: ")
                        print("✅ Nilai berhasil diubah.\n")
                    elif pilihan == '3':
                        data['kelas'] = input("Masukkan kelas baru: ")
                        print("✅ Kelas berhasil diubah.\n")
                    elif pilihan == '4':
                        data['jurusan'] = input("Masukkan jurusan baru: ")
                        print("✅ Jurusan berhasil diubah.\n")
                    elif pilihan == '5':
                        print("🔙 Batal ubah data.\n")
                        return
                    else:
                        print("❌ Pilihan tidak valid.\n")

                    lanjut = input("Ingin mengubah field lain untuk NIM ini? (y/n): ").lower()
                    if lanjut != 'y':
                        return
                return

        print("❌ NIM tidak ditemukan.")
        ulang = input("Ingin coba masukkan NIM lain? (y/n): ").lower()
        if ulang != 'y':
            print("🔙 Kembali ke menu utama.\n")
            return




def main():
    siswa = [
        {'nim': '10A', 'nama': 'Andi', 'nilai': '85', 'kelas': 'XII IPA 1', 'jurusan': 'IPA'},
        {'nim': '11B', 'nama': 'Budi', 'nilai': '78', 'kelas': 'XII IPS 2', 'jurusan': 'IPS'},
        {'nim': '12C', 'nama': 'Citra', 'nilai': '92', 'kelas': 'XII IPA 3', 'jurusan': 'IPA'},
        {'nim': '13D', 'nama': 'Dewi', 'nilai': '88', 'kelas': 'XII IPS 1', 'jurusan': 'IPS'},
        {'nim': '14E', 'nama': 'Eka', 'nilai': '90', 'kelas': 'XII IPA 2', 'jurusan': 'IPA'}
    ]

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            tampilkan_data(siswa)
        elif pilihan == '2':
            input_data(siswa)
        elif pilihan == '3':
            hapus_data(siswa)
        elif pilihan == '4':
            ubah_data(siswa)
        elif pilihan == '5':
            print("👋 Keluar dari program. Terima kasih!")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
