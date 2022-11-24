#~~~~~~~~~~
print ("~~~~~~~~~~/('v')\~~~~~~~~~~")
print ("PROGRAM PENGHITUNG VOLUME BANGUN RUANG")
print ("~~~~~~~~~~\('v')/~~~~~~~~~~")

print("pilihlah salah satu bangun ruang yang ingin di hitung volumenya:")
print("1. Limas")
print("2. Bola")
print("3. Prisma")
print("4. Kerucut")
print("")
pilihan = input("Masukkan pilihan anda: ")
if pilihan == '1':
#Limas
    alas = int(input("Masukkan panjang sisi alas limas: "))
    tinggi = int(input("Masukkan tinggi limas: "))
    hasil = ((alas*tinggi)/3)
    print ("volume limas tersebut adalah ", hasil)
elif pilihan == '2':
    jari = int(input("Masukkan panjang jari-jari bola: "))
    hasilbola = float(4/3*3.14*jari**3) 
    volume = print("volume bola tersebut adalah ", hasilbola)
elif pilihan == '3':
    print ("pilihlah salah satu dari pilihan di bawah:")
    print ("1. Prisma Segitiga")
    print ("2. Prisma Segiempat")
    print ("3. Prisma Segilima")
    opsilimas = input("Tentukan pilihan anda: ")
    if opsilimas == '1':
        sisialasprisma = int(input("Masukkan sisi alas prisma: "))
        alasprisma = int(input("Masukkan panjang  alas prisma: "))
        tinggiprisma = int(input("Masukkan tinggi prisma : "))
        hasilprisma = float((sisialasprisma*alasprisma/2)*tinggiprisma)
        print("volume prisma segitiga tersebut adalah", hasilprisma)
    elif opsilimas == '2':
        sisialasprisma1 = int(input("Masukkan sisi alas prisma: "))
        alasprisma1 = int(input("Masukkan panjang  alas prisma: "))
        tinggiprisma1 = int(input("Masukkan tinggi prisma : "))
        hasilprisma1 = float(sisialasprisma1*alasprisma1*tinggiprisma1)
        print ("volume prisma segi empat adalah", hasilprisma1)
    elif opsilimas == '3':
        sisialasprisma2 = int(input("Masukkan sisi alas prisma: "))
        alasprisma2 = int(input("Masukkan panjang  alas prisma: "))
        tinggiprisma2 = int(input("Masukkan tinggi prisma : "))
        hasilprisma2 = float((sisialasprisma2*alasprisma2*5)/2*tinggiprisma2)
        print ("volume prisma segi lima adalah", hasilprisma2)
    elif opsilimas == '5':
        print("Prisma yang anda cari belum tersedia di kalkulator ini")
    else :
        print("error")
elif pilihan == '4':
    jarikerucut = int(input("masukkan jari jari kerucut: "))
    tinggikerucut = int(input("masukkan tinggi kerucut: "))
    hasilkerucut = float(jarikerucut**2*3.14*tinggikerucut/3)
    print ("volume kerucut tersebut adalah : ", hasilkerucut)

        

else: 
    print ("error")
