import datetime

class mahasiswa:

    __nilai = 0
    jumlah_mahasiswa = 0

    while(True):
        def __init__(self, name = input('Masukkan Nama: '), nim = input('Masukkan Nim: ')):
            self.name = name
            self.nim = nim

            mahasiswa.jumlah_mahasiswa +=1

        try:
            def check_status(self, input_nilaiUTS = int(input("Masukkan Nilai UTS: ")), input_nilaiUAS = int(input("Masukkan Nilai UAS: "))):
                self.__nilai += input_nilaiUTS
                self.__nilai += input_nilaiUAS
                self.total = self.__nilai / 2

                if 80 <= self.total <= 100:
                    print(self.name,'Nilai anda adalah A')
                elif 68 <= self.total <= 79:
                    print(self.name, 'Nilai anda adalah B')
                elif 56 <= self.total <= 67:
                    print(self.name, 'Nilai anda adalah C')
                else:
                    print('Nilai anda adalah E')
        except:
            print('Inputan hanya berupa integer')

        jawab = input('ingin isi data lagi?')
        if jawab == 'tidak':
            break

zul = mahasiswa()
zul.check_status()
print(zul.__dict__)