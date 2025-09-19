#nilai yang diperoleh andi
nilai_tugas = int(input("masukkan nilai:"))
nilai_uts = int(input("masukkan nilai:"))
nilai_uas = int(input("masukkan nilai:"))

#Bobot nilai
bobot_tugas = 0.30
bobot_uts = 0.30
bobot_uas = 0.40 

#hitung nilai akhir
nilai_akhir = (nilai_tugas * bobot_tugas)+(nilai_uts * bobot_uts)+(nilai_uas * bobot_uas)

#tampilkan hasil
print("nilai akhirnya adalah :", nilai_akhir)
