jawab = 'yes'

while(True):
    a = input('Masukkan Nama: ')
    b = input('Masukkan Nim: ')
    mahasiswa = {'nama': a, 'nim': b}
    jawab = input('ulangi atau tidak?')
    if jawab == 'tidak':
        break

print('Daftar Mahasiswa', mahasiswa)
