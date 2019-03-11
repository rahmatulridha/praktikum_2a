# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:39:16 2019

@author: Nico Sembiring
"""

#Ketrampilan Pemrograman
#No.1
def jawabanNo1(npm):
    
    npm = list(str(npm))

    angka1 = {"0":" ###### ", "1":"  ##", "2":" #######  ", "3":"  #######  ", "4":"   #####", "5":"#######", "6":" #######", "7":"#######", "8":" ##### ", "9":" ######  "}
    angka2 = {"0":"###  ###", "1":"####", "2":"##    ### ", "3":"###     ###", "4":"  ##  ##", "5":"##     ", "6":"###     ", "7":"#######", "8":"##   ##", "9":"##    ## "}
    angka3 = {"0":"###  ###", "1":" ###", "2":"     ###  ", "3":"      #### ", "4":" ##   ##", "5":"##     ", "6":"###     ", "7":"   ### ", "8":" ##### ", "9":"##    ## "}
    angka4 = {"0":"###  ###", "1":" ###", "2":"    ###   ", "3":"      #### ", "4":"########", "5":"###### ", "6":"########", "7":"  ###  ", "8":"#######", "9":"######## "}
    angka5 = {"0":"###  ###", "1":" ###", "2":"  ####    ", "3":"###     ###", "4":"      ##", "5":"     ##", "6":"###  ###", "7":" ###   ", "8":"##   ##", "9":"      ## "}
    angka6 = {"0":" ###### ", "1":" ###", "2":"######### ", "3":"  #######  ", "4":"      ##", "5":"###### ", "6":" ###### ", "7":"###    ", "8":" ##### ", "9":"#######  "}
          
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
    while(hitung <96):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1


#no.3
def ulang3digitakhir(npm):
    hitung = 0
    npm = str(npm)
    x = npm[4:7]
    while(hitung < 15):
        print("Halo, " + x + " Apa Kabar?")
        hitung = hitung +1


#no.4
def digit3daribelakang(npm):
    npm = str(npm)
    x = npm[-3]
    print("Halo, " + x + " Apa Kabar?")


#no5
def kebawah(npm):
    for i in npm:
        print (i)
    


#no.6
def tambah(npm):
    jumlah = 0
    for i in npm:
        jumlah += int(i)
    print ("Hasil Penjumlahan NPM adalah : " +str(jumlah))


#No.7
def kali(npm):
    kalikan = 0
    for i in npm:
        kalikan *= int(i)
    print ("Hasil Perkalian NPM adalah : " +str(kalikan))


#N0.8
def digitgenap(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")


#No.9
def digitganjil(npm):
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")


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
