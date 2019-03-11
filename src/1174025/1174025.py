# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:45:34 2019

@author: dezha
"""

#Pemahaman Teori
#No.1
def namaFngsi(inputanFungsi):
    return inputanFungsi

output = namaFngsi("Kembalian Fungsi")
print(output)

#No.2
import math
print("Nilai i adalah: ", math.pi)

#No.3
class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
        
    def tampilProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()
        
mahasiswa1 = Mahasiswa("1174025", "Dezha Martha")
mahasiswa2 = Mahasiswa("1174026", "Jungle Supanti")

mahasiswa1.tampilProfil()
mahasiswa2.tampilProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#No.4
from file.Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174025", "Dezha Martha")
mhs2 = Mahasiswa("1174026", "Jungle Supanti")

mhs1.tampilProfil()
mhs2.tampilProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#No.5
from file.kalkulator import penambahan

hasil = penambahan(7, 6)
print(hasil)

#No.6
from file import kalkulator

a = 100
b = 50

hasil1 = kalkulator.penambahan(a, b)
hasil2 = kalkulator.pengurangan(a, b)
hasil3 = kalkulator.perkalian(a, b)
hasil4 = kalkulator.pembagian(a, b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#No.7
from file.Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174025", "Dezha Martha")
mhs2 = Mahasiswa("1174026", "Jungle Supanti")

mhs1.tampilProfil()
mhs2.tampilProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)



print(1174025%3)
#Ketrampilan Pemrograman
#No.1
def jawabanNo1():
    
    npm = input("Masukan NPM :")
    npm = list(str(npm))

    angka1 = {"0":" ++++++ ", "1":"  ++", "2":" +++++++  ", "3":"  +++++++  ", "4":"   +++++", "5":"+++++++", "6":" +++++++", "7":"+++++++", "8":" +++++ ", "9":" ++++++  "}
    angka2 = {"0":"+++  +++", "1":"++++", "2":"++    +++ ", "3":"+++     +++", "4":"  ++  ++", "5":"++     ", "6":"+++     ", "7":"+++++++", "8":"++   ++", "9":"++    ++ "}
    angka3 = {"0":"+++  +++", "1":" +++", "2":"     +++  ", "3":"      ++++ ", "4":" ++   ++", "5":"++     ", "6":"+++     ", "7":"   +++ ", "8":" +++++ ", "9":"++    ++ "}
    angka4 = {"0":"+++  +++", "1":" +++", "2":"    +++   ", "3":"      ++++ ", "4":"++++++++", "5":"++++++ ", "6":"++++++++", "7":"  +++  ", "8":"+++++++", "9":"++++++++ "}
    angka5 = {"0":"+++  +++", "1":" +++", "2":"  ++++    ", "3":"+++     +++", "4":"      ++", "5":"     ++", "6":"+++  +++", "7":" +++   ", "8":"++   ++", "9":"      ++ "}
    angka6 = {"0":" ++++++ ", "1":" +++", "2":"+++++++++ ", "3":"  +++++++  ", "4":"      ++", "5":"++++++ ", "6":" ++++++ ", "7":"+++    ", "8":" +++++ ", "9":"+++++++  "}
          
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []

    for x in npm:
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ')
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')

jawabanNo1()

#no.2
def ulang(npm):
    hitung = 0
    while(hitung <25):
        print("Halo there, " + str(npm) + " wat shup?")
        hitung = hitung +1
ulang(int(input("Masukkan NPM: ")))

#no.3
def ulang3digitakhir(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 7):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1
ulang3digitakhir(int(input("Masukkan NPM: ")))

#no.4
def digit3daribelakang(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar anda?")
digit3daribelakang(int(input("Masukkan NPM: ")))

#no5
def kebawah(npm):
    for i in npm:
        print (i)
    
kebawah(input("Masukkan NPM: "))

#no.6
def tambah(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))
tambah(input("Masukkan NPM: "))

#No.7
def kali(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))
kali(input("Masukkan NPM: "))

#N0.8
def digitgenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
digitgenap(input("Masukkan NPM: "))

#No.9
def digitganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
digitganjil(input("Masukkan NPM: "))

#No.10
def digitprima(npm):
    npm = list(map(int, npm))
    prima = []
    for n in npm:
        bilPrima = True
        if n == 0 or n ==1:
            bilPrima = False
        for x in range(2, n):
            if n % x == 0:
                bilPrima = False
        if bilPrima:
            prima.append(n)
                
        for p in prima:
            print(p, end = "")
digitprima(input("Masukkan NPM: "))

#No.11

#No.12

#Keterampilan Penanganan error
def halo(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Ada yang error nih")
        
halo(input("Nama ei nama : "))
