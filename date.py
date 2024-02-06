# date and time

import datetime as dete

print('input tanggal lahir anda: ')
tgl = int(input('Tanggal \t: '))
bln = int(input('Bulan \t\t: '))
thn = int(input('Tahun \t\t: '))

tgl_lhr = dete.date(thn, bln, tgl)
print(f'tanggal lahir ku adalah : {tgl_lhr}')
print(f'harinya adalah : {tgl_lhr:%A}')
hariIni = dete.date.today()
print(f'hari ini adalah tanggal : {hariIni}')
selisih = hariIni - tgl_lhr
thn = selisih.days // 365
bln_selisih = (selisih.days % 365) // 30
tgl_selisih = ((selisih.days % 365) % 30) % 30
print(f'umur saya hari ini adalah : {thn} tahun, {bln_selisih} bulan, {tgl_selisih} hari')