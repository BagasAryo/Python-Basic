# continue, pass and break

# 1. pass -> berfungsi sebagai dummy, tidak akan dieksekusi
angka = 0
while angka < 3:
    angka += 1
    if angka == 2:
        pass
        # print('love u')
    print(angka)
print('\n')
# 2. continue -> berfungsi sebagai
kelas = 7
while kelas > 2:
    kelas -= 1
    print(f'mantap {kelas}')
    if kelas == 5:
        print(f'angka {kelas}!')
        continue # semua perintah yang ada dibawahnya akan di skip dan mengulang dari awal
    print('diluar if')
print('keluar while')