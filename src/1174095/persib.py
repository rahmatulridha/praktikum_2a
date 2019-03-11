# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 19:27:32 2019

@author: dzihan
"""
#fungsi
def dadah():
    print("Dadah Radovic")

dadah()

#input
def pelatih(persib):
    print("Pelatih idola kamu :"+str(persib))

pelatih(input("Masukan Nama Pelatih : "))

#kembalian
def kembalian(a,b):
    r = a + b
    return r

a = 10
b = 50
c = kembalian(a,b)
print(c)

import math
print("Nilai pi adalah: ", math.pi)

class Sepeda:
    jumlahSepeda = 0
    
    def __init__(self, nama):
        self.nama = nama
        Sepeda.jumlahSepeda +=1
            
    def tampilkanSepeda(self):
        print("nama :", self.nama)
        print()

sepeda1 = Sepeda("United")
sepeda2 = Sepeda("Polygon")

sepeda1.tampilkanSepeda()
sepeda2.tampilkanSepeda()

print("Sepedanya ", Sepeda.jumlahSepeda)

#3
from Sepeda import Sepeda

sepeda1 = Sepeda("United")
sepeda2 = Sepeda("Polygon")

sepeda1.tampilkanSepeda()
sepeda2.tampilkanSepeda()

print("Sepedanya ", Sepeda.jumlahSepeda)
#4
from Sepeda import Sepeda
#5
from Berhitunglah import Penambahan

hasil = Penambahan(10, 5)

print(hasil)
#6
from folderdj import Berhitunglah

a=12
b=50

hasil1=Berhitunglah.Penambahan(a,b)
hasil2=Berhitunglah.Pengurangan(a,b)
hasil3=Berhitunglah.Perkalian(a,b)
hasil4=Berhitunglah.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

from folderdj.Sepeda import Sepeda

sepeda1 = Sepeda("United")
sepeda2 = Sepeda("Polygon")

sepeda1.tampilkanSepeda()
sepeda2.tampilkanSepeda()

print("Sepedanya ", Sepeda.jumlahSepeda)