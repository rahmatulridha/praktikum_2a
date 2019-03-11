class bunga:
    jumlahbunga = 0
    
    def __init__(self, nama):
        self.nama = nama
        bunga.jumlahbunga +=1
            
    def tampilkanbunga(self):
        print("Nama :", self.nama)
        print()

bunga1 = bunga("Mawar")
bunga2 = bunga("Melati")
bunga3 = bunga("Kamboja")

bunga1.tampilkanbunga()
bunga2.tampilkanbunga()
bunga3.tampilkanbunga()

print("Total Bunganya adalah: ", bunga.jumlahbunga)