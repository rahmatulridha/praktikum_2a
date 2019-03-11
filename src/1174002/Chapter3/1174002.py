# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:42:18 2019

@author: Habib Abdul R
"""
#Teori
#Pemahaman Teori
#Jawaban No. 1
def namaFungsi(inputanFungsi):
    return inputanFungsi

output = namaFungsi("Kembalian Fungsi")
print(output)

#Jawaban No. 2
import math
print("Nilai pi adalah: ", math.pi)

#Jawaban No. 3
class Mahasiswa:
    jumlahMahasiswa = 0
    
    def __init__(self, npm, nama):
        self.npm = npm
        self.nama = nama
        Mahasiswa.jumlahMahasiswa +=1
            
    def tampilkanProfil(self):
        print("NPM :", self.npm)
        print("Nama :", self.nama)
        print()

mahasiswa1 = Mahasiswa("1174002", "Habib Abdul Rasyid")
mahasiswa2 = Mahasiswa("1174099", "Abdul Rasyid")

mahasiswa1.tampilkanProfil()
mahasiswa2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 4
from Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174002", "Habib Abdul Rasyid")
mhs2 = Mahasiswa("1174099", "Abdul")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)

#Jawaban No. 5
from kalkulator import Penambahan

hasil = Penambahan(10, 5)
print(hasil)

#Jawaban No. 6
from folder import kalkulator

a=50
b=25

hasil1=kalkulator.Penambahan(a,b)
hasil2=kalkulator.Pengurangan(a,b)
hasil3=kalkulator.Perkalian(a,b)
hasil4=kalkulator.Pembagian(a,b)

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)

#Jawaban No. 7
from folder.Mahasiswa import Mahasiswa

mhs1 = Mahasiswa("1174002", "Habib Abdul Rasyid")
mhs2 = Mahasiswa("1174099", "Abdul")

mhs1.tampilkanProfil()
mhs2.tampilkanProfil()

print("Total mahasiswa adalah ", Mahasiswa.jumlahMahasiswa)


#Ketrampilan Pemrograman
#No.1
def jawabanNo1():
    
    npm = input("Masukan NPM :")
    npm = list(str(npm))

    angka1 = {"0":" ****** ", "1":"  **", "2":" *******  ", "3":"  *******  ", "4":"   *****", "5":"*******", "6":" *******", "7":"*******", "8":" ***** ", "9":" ******  "}
    angka2 = {"0":"***  ***", "1":"****", "2":"**    *** ", "3":"***     ***", "4":"  **  **", "5":"**     ", "6":"***     ", "7":"*******", "8":"**   **", "9":"**    ** "}
    angka3 = {"0":"***  ***", "1":" ***", "2":"     ***  ", "3":"      **** ", "4":" **   **", "5":"**     ", "6":"***     ", "7":"   *** ", "8":" ***** ", "9":"**    ** "}
    angka4 = {"0":"***  ***", "1":" ***", "2":"    ***   ", "3":"      **** ", "4":"********", "5":"****** ", "6":"********", "7":"  ***  ", "8":"*******", "9":"******** "}
    angka5 = {"0":"***  ***", "1":" ***", "2":"  ****    ", "3":"***     ***", "4":"      **", "5":"     **", "6":"***  ***", "7":" ***   ", "8":"**   **", "9":"      ** "}
    angka6 = {"0":" ****** ", "1":" ***", "2":"******** ", "3":"  ********  ", "4":"      **", "5":"****** ", "6":" ****** ", "7":"***    ", "8":" ***** ", "9":"*******  "}
          
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
def jawabanNo2(npm):
    hitung = 0
    while(hitung < 2):
        print("Hello, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
jawabanNo2(int(input("Masukkan NPM: ")))

#no.3
def jawabanNo3(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 2):
        print("Hello, " + x + " Apa Kabar?")
        hitung = hitung +1
jawabanNo3(int(input("Masukkan NPM: ")))

#no.4
def jawabanNo4(npm):
    npm = str(npm)
    x = npm[-3]
    print("Hello, " + x + " Apa Kabar?")
jawabanNo4(int(input("Masukkan NPM: ")))

#no5
def jawabanNo5(npm):
    for i in npm:
        print (i)
    
jawabanNo5(input("Masukkan NPM: "))

#no.6
def jawabanNo6(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))
jawabanNo6(input("Masukkan NPM: "))

#No.7
def jawabanNo7(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))
jawabanNo7(input("Masukkan NPM: "))

#N0.8
def jawabanNo8(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
jawabanNo8(input("Masukkan NPM: "))

#No.9
def jawabanNo9(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
jawabanNo9(input("Masukkan NPM: "))

#No.10
def jawabanNo10(npm):
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
jawabanNo10(input("Masukkan NPM: "))

#No.11

#No.12

#Keterampilan Penanganan error
#No.1
def halo(nama):
    try:
        print("Hallo, "+str(nama))
    except:
        print("Ada Yang Error")
        
halo(input("Cantumkan Nama Anda : "))
