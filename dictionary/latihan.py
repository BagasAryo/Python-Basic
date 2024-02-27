# latihan dictionary part 1
import datetime

mhs_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mhs = {}

print(f'{"SELAMAT DATANG!":^35}')
print(f'{"SILAHKAN ISI DATA DIRI ANDA":^35}')

mhs = dict.fromkeys(mhs_template.keys())
print(mhs)
mhs['nama'] = input('input nama mahasiswa: ')
mhs['nim'] = input('input nim: ')
mhs['sks'] = input('input sks: ')
TAHUN_LAHIR = int(input('input tahun lahir: '))
BULAN_LAHIR = int(input('input bulan lahir: '))
HARI_LAHIR = int(input('input tanggal lahir: '))
mhs['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, HARI_LAHIR)
print(mhs)