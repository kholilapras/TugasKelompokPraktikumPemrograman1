while True:
    print("\n<=><=><=><=>| MENCARI NILAI RERATA DAN RANKING SISWA |<=><=><=><=>")

    # Input jumlah total siswa
    while True:
        try:
            total_siswa = int(input("Masukkan Jumlah Total Siswa : "))
            break
        except ValueError:
            print("Masukkan angka yang valid !")

    # Input jumlah banyak nilai nilai
    while True:
        try:
            jumlah_banyaknya_nilai = int(input("Masukkan Jumlah Banyaknya Nilai : "))
            break
        except ValueError:
            print("Masukkan angka yang valid !")

    total_persentase = 0

    while total_persentase != 100:
        banyaknya_nilai_total = []
        persentase_nilai = []
        total_persentase = 0

        # Input nama dan persentase banyak nilai nilai
        for i in range(jumlah_banyaknya_nilai):
            banyak_nilai = input(f"\nMasukkan Nama Nilai Ke-{i+1} : ")
            while True:
                try:
                    persentase = int(input(f"Masukkan Persentase Nilai Ke-{i+1} (0-100) : "))
                    if persentase < 0 or persentase > 100:
                        print("Persentase nilai harus berada dalam rentang 0-100")
                    else:
                        total_persentase += persentase
                        break
                except ValueError:
                    print("Masukkan angka yang valid !")
            banyaknya_nilai_total.append(banyak_nilai)
            persentase_nilai.append(persentase)

        if total_persentase != 100:
            print("Total persentase banyak nilai harus 100! Silakan input ulang")

    # Menginisialisasi daftar siswa
    siswa = []

    # Input data setiap siswa
    for i in range(total_siswa):
        print(f"\n=====| INPUT DATA SETIAP SISWA |=====")
        print(f"Siswa Ke {i+1} Dari {total_siswa}")
        nama = input("Nama Lengkap : ")
        nomor = input("Nomor : ")

        # Menginisialisasi daftar banyak nilai
        banyak_nilai = []

        # Input nilai setiap banyak_nilai
        for j in range(jumlah_banyaknya_nilai):
            while True:
                try:
                    nilai = int(input(f"Nilai {banyaknya_nilai_total[j]}[{persentase_nilai[j]}%] (0-100) : "))
                    if nilai < 0 or nilai > 100:
                        print("Nilai harus berada dalam rentang 0-100 !")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang valid !")
            banyak_nilai.append(nilai)

        siswa.append({
            'nama': nama,
            'nomor': nomor,
            'banyak_nilai': banyak_nilai
        })

    # Menghitung rata-rata dan nilai akhir setiap siswa
    for siswa_data in siswa:
        total_nilai = 0
        for j in range(jumlah_banyaknya_nilai):
            total_nilai += siswa_data['banyak_nilai'][j] * persentase_nilai[j] / 100
        siswa_data['nilai_akhir'] = total_nilai

    # Mengurutkan siswa berdasarkan nilai akhir secara menurun
    siswa.sort(key=lambda x: x['nilai_akhir'], reverse=True)

    # Cetak hasil rata-rata dan ranking siswa
    print("\n=====| HASIL RERATA DAN RANKING SISWA |=====")
    print("No | Nama Lengkap : No |", end=" ")
    for banyak_nilai in banyaknya_nilai_total:
        print(banyak_nilai, end=" | ")
    print("= [Rerata]")

    for i, siswa_data in enumerate(siswa):
        print(f"{i+1} | {siswa_data['nama']} : {siswa_data['nomor']} |", end=" ")
        for nilai in siswa_data['banyak_nilai']:
            print(nilai, end=" | ")
        print(f"= [{siswa_data['nilai_akhir']:.2f}]")
        
    # Looping program
    while True:
        ulangi = input("\nApakah Anda Ingin Mencari Nilai Rerata Dan Ranking Siswa Lagi (Y/N) : ")
        if ulangi.lower() == 'y' or ulangi.lower() == 'n':
            break
        else:
            print("Masukkan 'Y' untuk ya atau 'N' untuk tidak.")

    if ulangi.lower() != 'y':
        break