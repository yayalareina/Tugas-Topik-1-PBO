class sepeda:
    def __init__ (self, merk, warna, harga):
        self.merk = merk
        self.warna = warna
        self.harga = harga
        self.kecepatan = 0

    def kayuh(self, kecepatan):
        self.kecepatan += kecepatan
        print("sepeda melaju dengan kecepatan", self.kecepatan, "km/jam")

    def rem(self):
        self.kecepatan = 0
        print("sepeda berhenti")

    def belok(self, arah):
        print("sepeda belok ke", arah)

#Contoh penggunaan kelas Sepeda
sepeda_saya = sepeda("Polygon", "Merah", 5000000)

sepeda_saya.kayuh(20)
sepeda_saya.belok("kiri")
sepeda_saya.kayuh(10)
sepeda_saya.rem()