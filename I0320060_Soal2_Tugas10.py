#soal 2

print("Program Biodata Diri")
print("="*50)
print()
print("Biodata Mahasiswa Teknik Industri UNS")
print("="*50)
print()
print("Silahkan input data diri anda!")
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
angkatan = int(input("Angkatan: "))
umur = int(input("Umur: "))
alamat = input("Alamat: ")

#format teks
teks = "Nama: {}\nNIM: {}\nKelas: {}\nAngkatan: {}\nUmur: {}\nAlamat: {}".format(nama,nim,kelas,angkatan,umur,alamat)

#buka file
file_Bio = open("Biodata.txt","w")

#tulis teks
file_Bio.write(teks)

#tutup file
file_Bio.close()