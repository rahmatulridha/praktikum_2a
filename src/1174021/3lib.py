#3.3 Ketrampilan Pemrograman
#Soal no.1

def soalno1():
    npm = input("Masukkan NPM :")
    npm = list(str(npm))
    
    angka1={"0":"*********", "1":"***",  "2":"**********", "3":"**********", "4":"***     ***", "5":"**********", "6":"**********", "7":"**********", "8":"**********", "9":"**********"}
    angka2={"0":"*********", "1":"***",  "2":"**********", "3":"**********", "4":"***     ***", "5":"**********", "6":"**********", "7":"**********", "8":"**********", "9":"**      **"}
    angka3={"0":"**     **", "1":"***",  "2":"       ***", "3":"       ***", "4":"***     ***", "5":"***       ", "6":"***       ", "7":"        **", "8":"**      **", "9":"**      **"}
    angka4={"0":"**     **", "1":"***",  "2":"       ***", "3":"       ***", "4":"***     ***", "5":"***       ", "6":"***       ", "7":"       ***", "8":"**      **", "9":"**********"}
    angka5={"0":"**     **", "1":"***",  "2":"**********", "3":"**********", "4":"***********", "5":"**********", "6":"**********", "7":"      *** ", "8":"**********", "9":"**********"}
    angka6={"0":"**     **", "1":"***",  "2":"***       ", "3":"       ***", "4":"        ***", "5":"       ***", "6":"**      **", "7":"     ***  ", "8":"**      **", "9":"        **"}
    angka7={"0":"**     **", "1":"***",  "2":"***       ", "3":"       ***", "4":"        ***", "5":"       ***", "6":"**      **", "7":"    ***   ", "8":"**      **", "9":"        **"}
    angka8={"0":"*********", "1":"***",  "2":"**********", "3":"**********", "4":"        ***", "5":"**********", "6":"**********", "7":"   ***    ", "8":"**********", "9":"**********"}
    angka9={"0":"*********", "1":"***",  "2":"**********", "3":"**********", "4":"        ***", "5":"**********", "6":"**********", "7":"  ***     ", "8":"**********", "9":"**********"}
    
    hasil1 = []
    hasil2 = []
    hasil3 = []
    hasil4 = []
    hasil5 = []
    hasil6 = []
    hasil7 = []
    hasil8 = []
    hasil9 = []
    
    for x in npm :
        hasil1.append(angka1[x])
        hasil2.append(angka2[x])
        hasil3.append(angka3[x])
        hasil4.append(angka4[x])
        hasil5.append(angka5[x])
        hasil6.append(angka6[x])
        hasil7.append(angka7[x])
        hasil8.append(angka8[x])
        hasil9.append(angka9[x])
    
    print(*hasil1, sep=' ')
    print(*hasil2, sep=' ')
    print(*hasil3, sep=' ') 
    print(*hasil4, sep=' ')
    print(*hasil5, sep=' ')
    print(*hasil6, sep=' ')
    print(*hasil7, sep=' ') 
    print(*hasil8, sep=' ') 
    print(*hasil9, sep=' ') 

soalno1()

#Soal no.2
def soalno2() : 
    npm = input("Masukan NPM :")
    npm = (str(npm))
    hitung = 0
    while(hitung < 21):
        print("Halo, " + str(npm) + " Apa Kabar?")
        hitung = hitung +1
        
soalno2()

#Soal no.3
def soalno3() :
    npm = input("Masukan NPM : ")
    npm = (str(npm))
    hitung = 0
    while(hitung < 0+2+1):
        print("Halo, " + str(npm[4:7]) + " Apa Kabar?")
        hitung = hitung +1
        
soalno3()

#Soal no.4
def soalno4() :
    npm = input("Masukan NPM : ")
    npm = (str(npm))
    i = 0
    if(i < 1):
        print("Halo, " + str(npm[2]) + " Apa Kabar?")
soalno4()    

#Soal no.5
def soalno5() :
    npm = input("Masukkan NPM: ")
    npm = (str(npm))
    
    for i in npm:
        print (i)
    
soalno5()

#Soal no.6
def soalno6() :
    npm = input("Masukkan NPM: ")
    hasil = 0
    for i in npm:
        hasil += int(i)
    print(str(hasil)+" Adalah hasil perkalian dari "+ (npm))

soalno6()

#Soal no.7
def soalno7() :
    npm = input("Masukkan NPM: ")
    hasil = 0
    for i in npm:
        hasil *= int(i)
    print(str(hasil)+" Adalah hasil perkalian dari "+ (npm))

soalno7()

#Soal no.8
def soalno8() :
    npm = input("Masukkan NPM: ")
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 == 0):
            if(n != 0):
                print(n, end ="")
soalno8()

#Soal no.9
def soalno9() :
    npm = input("Masukkan NPM: ")
    npm = str(npm)
    npm = list(map(int, npm))
    for n in npm:
        if(n % 2 !=0):
            print(n, end ="")
            
soalno9()

#Soal no.10
def soalno10() :
    npm = input("Masukkan NPM: ")
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

soalno10()