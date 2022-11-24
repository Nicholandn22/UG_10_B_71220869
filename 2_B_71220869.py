print ("=========== PROGRAM PENGHITUNG PHYTAGORAS ===========")
p1 = int(input("masukkan bilangan bulat pertama :"))
p2 = int(input("masukkan bilangan bulat kedua :"))
p3 = int(input("masukkan bilangan bulat ketiga :"))
hasil = ((p1**2)+(p2**2))
hasil1 = (p2**2+p3**2)
if hasil == (p3**2):
    print ("merupakan phytagoras")
elif hasil1 == p1:
    print("merupakan phytagoras")
else :
    print("bukan merupakan phytagoras")

