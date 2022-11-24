print ("Selamat Datang Di Program Pengurutan Bilangan")
print ("")
print ("Silahkan Pilih Metode Yang Akan Dipakai")
print ("1. Ascending")
print ("2. Descending")
print ("")
opsi1 = int(input(">> "))
print ("")

if opsi1 == 1:
    opsi1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    opsi2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    opsi3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    opsi4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    list1 = [opsi1 , opsi2 , opsi3 , opsi4]
    print ("Urutan angka anda ", sorted(list1))
elif opsi1 == 2:
    opsi1 = int(input("Masukan Bilangan Bulat Pertama >> "))
    opsi2 = int(input("Masukan Bilangan Bulat Kedua >> "))
    opsi3 = int(input("Masukan Bilangan Bulat Ketiga >> "))
    opsi4 = int(input("Masukan Bilangan Bulat Keempat >> "))
    list2 = [opsi1 , opsi2 , opsi3 , opsi4]
    print ("Urutan angka anda ", sorted(list2,reverse=True))
else:
    print ("Input anda salah")