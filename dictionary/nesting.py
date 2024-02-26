# multikeys and nesting dictionary

import datetime

mhs1 = {
    'nama': 'Bagas Aryo',
    'nim': 'a1114756',
    'sks': 24,
    'beasiswa': True,
    'lahir': datetime.datetime(2004, 3, 23)
}

mhs2 = {
    'nama': 'Amanda Puspita',
    'nim': 'a1114758',
    'sks': 22,
    'beasiswa': True,
    'lahir': datetime.datetime(2004, 10, 23)
}

mhs3 = {
    'nama': 'Azizi Asadel',
    'nim': 'a1114759',
    'sks': 23,
    'beasiswa': False,
    'lahir': datetime.datetime(2004, 12, 25)
}

data_mhs = {
    'MHS01': mhs1,
    'MHS02': mhs2,
    'MHS03': mhs3
}

# < : rata kiri, > : rata kanan, ^ : center
print(f"{'KEY':<5} {'Nama':<15}{'NIM':<9} {'SKS':<3} {'Beasiswa':<6} {'Tgl Lahir':<10}")
print('-'*60)

for mhs in data_mhs:
    KEY = mhs
    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs[KEY]['nim']
    SKS = data_mhs[KEY]['sks']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime('%x')

    print(f"{KEY:<5} {NAMA:<15} {NIM:<9} {SKS:<3} {BEASISWA:<8} {LAHIR:<10}")