# continue, pass and break

# 1. pass -> berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 3:
    angka += 1
    if angka == 2:
        pass
        print('love u')
    print(angka)
print('\n')

# 2. continue -> berfungsi untuk menunda perintah yang berada setelah continue yang berada di satu perulangan dan berpindah ke iterasi selanjutnya
kelas = 7
while kelas > 2:
    kelas -= 1
    print(f'mantap {kelas}')
    if kelas == 5:
        print(f'angka {kelas}!')
        continue  # semua perintah yang ada dibawahnya akan di skip dan mengulang dari awal
    print('diluar if')
print('keluar while')
print('\n')

# 3. Break -> berfungsi untuk mengakhiri/keluar dari suatu looping yang sekarang dan melanjutkan perintah selanjutnya
angkaBreak = 0
while angkaBreak < 5:
    angkaBreak += 1
    print(f'angka sekarang sedang berada di angka {angkaBreak}')
    if angkaBreak == 3:
        print('mantap')
        break
    print('apakabar')
print('akhiru kalam')
print('\n')

# 4.1. latihan perulangan menggunakan for
print('====LATIHAN LOOPING====')
colfor = int(input('masukkan nilai panjang: '))
rowfor = 1
for i in range(colfor):
    print('*' * rowfor)
    rowfor += 1

# 4.2. latihan perulangan menggunakan while
colwhile = int(input('masukkan nilai panjang by while: '))
rowwhile = 1
while True:
    print('*' * rowwhile)
    rowwhile += 1
    if rowwhile > colwhile:
        break

# 4.3. latihan perulangan menggunakan while hanya ganjil
colodd = int(input('masukkan nilai panjang by while odd: '))
rowodd = 1
while True:
    if not(rowodd % 2):
        rowodd += 1
        continue

    if rowodd > colodd:
        break

    print('*' * rowodd)
    rowodd += 1

# 4.4 latihan perulangan menggunakan while mid
print('\nWHILE PYRAMID')
colmid = 10
rowmid = 1
space = int(colmid/2)

while True:
    if not(rowmid % 2):
        rowmid += 1
        continue

    if rowmid > colmid:
        break

    print(' '*space,'*' * rowmid)
    space -= 1
    rowmid += 1