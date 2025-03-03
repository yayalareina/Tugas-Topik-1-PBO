class Mahasiswa:
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.sks_terkumpul = 0
        self.ipk = 0.0

    def ambil_sks(self, jumlah_sks):
        self.sks_terkumpul += jumlah_sks
        print(f"{self.nama} telah mengambil {jumlah_sks} SKS. Total SKS sekarang: {self.sks_terkumpul}")

    def perbarui_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        print(f"IPK {self.nama} diperbarui menjadi {self.ipk}")

    def info(self):
        print(f"Mahasiswa {self.nama} dengan NIM {self.nim} dari jurusan {self.jurusan} memiliki IPK {self.ipk} dan telah mengumpulkan {self.sks_terkumpul} SKS.")

# Contoh penggunaan
mahasiswa1 = Mahasiswa("Annetha", "20202345", "Teknik Informatika")
mahasiswa1.info()
mahasiswa1.ambil_sks(20)
mahasiswa1.perbarui_ipk(3.75)
mahasiswa1.info()
