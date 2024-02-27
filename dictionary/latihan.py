# latihan dictionary part 1
import datetime
import os
import string
import random

mhs_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mhs = {}
# untuk menghilangkan path directory pada terminal ketika program dijalankan
os.system('cls')
while True:
    print(f'{"SELAMAT DATANG!":^35}')
    print(f'{"SILAHKAN ISI DATA DIRI ANDA":^35}')

    mhs = dict.fromkeys(mhs_template.keys())
    # print(mhs)
    mhs['nama'] = input('input nama mahasiswa: ')
    mhs['nim'] = input('input nim: ')
    mhs['sks'] = input('input sks: ')
    TAHUN_LAHIR = int(input('input tahun lahir: '))
    BULAN_LAHIR = int(input('input bulan lahir: '))
    HARI_LAHIR = int(input('input tanggal lahir: '))
    mhs['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, HARI_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase)) for i in range(6))
    data_mhs.update({KEY: mhs})

# latihan part 2
    print(f"{'KEY':<6} {'Nama':<17} {'NIM':<9} {'SKS':<3} {'Tgl Lahir':<10}")
    print('-'*60)
    for mhs in data_mhs:
        KEY = mhs

        NAMA = data_mhs[KEY]['nama']
        NIM = data_mhs[KEY]['nim']
        SKS = data_mhs[KEY]['sks']
        LAHIR = data_mhs[KEY]['lahir'].strftime('%x')

        print(f"{KEY:<6} {NAMA:<17} {NIM:<9} {SKS:<3} {LAHIR:<10}")

    print('\n')
    is_done = input('Ingin melakukan input lagi?')

    print('\n')
    if is_done == 'n':
        break

print('program selesai')
