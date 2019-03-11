# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:24:58 2019

@author: dzihan
"""

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
