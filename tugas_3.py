# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:06:54 2019

@author: Aegis
"""
#No 1
print("###  ###  ###########  ###   ###  #########  ###  ###########")
print("###  ###  ###########  ###   ###  #########  ###  ###########")
print("###  ###         ###   ###   ###  ##     ##  ###  ###		")
print("###  ###        ###    ###   ###  ##     ##  ###  ###		")
print("###  ###       ###     #########  ##     ##  ###  ###########")
print("###  ###      ###            ###  ##     ##  ###  ###########")
print("###  ###     ###             ###  ##     ##  ###          ###")
print("###  ###    ###              ###  ##     ##  ###          ###")
print("###  ###   ###               ###  #########  ###  ###########")
print("###  ###  ###                ###  #########  ###  ###########")

def penulisan (npm):
	if npm%3 == 0:
		for i in range (npm) :
			print ("*")
	elit npm%3 == 1:
	    for i in range (npm) :
	    	print("#")
	elit npm%3 == 2:
	    for i in range (npm) :
	    	print("+")
	else :
		print ("Tidak ditemukan")

#penulisan(int(input("masukkan NPM :")))

#No2
def perulangan (npm) :
	hitung = 0
	while (hitung < 27) :
		print ("halo, "+str(npm)+" apa kabar?")

#perulangan(int(input("masukkan NPM :")))

#No3
def perulangan)_3_digit(npm):
	hitung = 0
	npm = str (npm)
	bil = npm[4:7]

	while(hitung < 9):
		print("halo, "+bil+"apa kabar?")

#perulangan(int(input("masukkan NPM :")))

#No4
def perulangan_3_digit_terakhir(npm):
	npm = str (npm)
	bil = npm[-3]
	print (" halo,"+bil+"apa kabar?")

#perulangan_3_digit_terakhir(int(input("masukkan NPM :")))

#No5
def down (npm):
	for i in npm:
		print (i)

#down(input("masukkan NPM :"))

#No6
def penjumlahan(NPM):
	jumlah = 0
	for i in npm :
		jumlah +=int(i)
		print(str(jumlah)+ "adalah hasil penjumlahan")

#penjumlahan(input("masukkan NPM :"))

#No7
def perkalian(npm):
	jumlah = 0
	for i in npm:
		jumlah *= int (i)
		print(str(jumlah)+ "adalah hasil perkalian")

#perkalian(input("masukkan NPM :"))

#No8
def genap(npm):
	for i in range(1,int (npm)+1):
		if i % 2 ==0:
			print(i)
			
#genap(int(input("masukkan NPM :")))

#No 9 
def ganjil():
    npm = [1,1,7,4,0,1,5]
    for i in npm:
        if (i%2)==1:
            print("Bilangan Ganjilnya : "+str(i))
ganjil()

#ganjil(int(input("masukkan NPM :")))

#No 10
def prima(npm):
    npm = str(npm)
    bil = npm[2]
    num = int(bil)
    if num > 1:
        for i in range(2,num):
            if (num%i)==0:
                print("Bukan Bilangan Prima")
                break
            else:
                print("Bilangan Primanya :"+str(num))
    else:
        print("Tidak Ada Bilangan Prima")
prima(int(input("Masukan NPM : "))) 







