# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:59:22 2019

@author: user
"""

lib =  __import__('3lib')

npm = "1174005"

hasil1 = lib.jawabanNo1(npm)
hasil2 = lib.ulang(npm)
hasil3 = lib.ulangdigitterakhir(npm)
hasil3 = lib.ulangdigitdaribelakang(npm)
hasil3 = lib.kebawah(npm)
hasil3 = lib.tanbah(npm)
hasil3 = lib.kali(npm)
hasil3 = lib.ulangdigitgenap(npm)
hasil3 = lib.ulangdigitganjil(npm)
hasil3 = lib.ulangdigitprima(npm)

from kelas3lib import kelas3lib

npm = "1174005"

kelas3lib = kelas3lib(npm)

kelas3lib.JawabanNo1()
kelas3lib.Ulang()
kelas3lib.Ulang3digitterakhir()
kelas3lib.Digit3daribelakang()
kelas3lib.Kebawah()
kelas3lib.Tambah()
kelas3lib.Kali()
kelas3lib.Digitgenap()
kelas3lib.Digitganjil()
kelas3lib.Digitprima()