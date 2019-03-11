# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 21:51:34 2019

@author: Nico Sembiring
"""

lib = __import__('3lib')

npm = "1174096"

hasil1 = lib.jawabanNo1(npm)
hasil2 = lib.ulang(npm)
hasil3 = lib.ulang3digitakhir(npm)
hasil4 = lib.digit3daribelakang(npm)
hasil5 = lib.kebawah(npm)
hasil6 = lib.tambah(npm)
hasil7 = lib.kali(npm)
hasil8 = lib.digitgenap(npm)
hasil9 = lib.digitganjil(npm)
hasil10 = lib.digitprima(npm)

from kelas3lib import kelas3lib

npm = "1174096"

kelas3lib = kelas3lib(npm)

kelas3lib.JawabanNo1()
kelas3lib.Ulang()
kelas3lib.Ulang3digitakhir()
kelas3lib.Digit3daribelakang()
kelas3lib.Kebawah()
kelas3lib.Tambah()
kelas3lib.Kali()
kelas3lib.Digitgenap()
kelas3lib.Digitganjil()
kelas3lib.Digitprima()
