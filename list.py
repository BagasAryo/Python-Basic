# initially list

data_angka = [1, 2, 3, 4, 6]
print(data_angka)

data_str = ['satu', 'tiga', 'empat', 'enam']
print(data_str)

data_bool = [True, False, True, True]
print(data_bool)

data_mix = [1, 2, 'tiga', 'empat', False, False]
print(data_mix)

# alternate make some list
data_range = range(0, 10, 2)
print(data_range)

data_list = list(data_range)
print(data_list)

# make a list from for
list_for = [i+1 for i in range(0, 10)]
print(list_for)

list_for_if = [i for i in range(0, 10) if i % 2 == 1]
print(list_for_if)


# Manipulate data
# 1. operasi
data = ['muh', 'fifhal', 'elang', 'satria']
print(f'\n{data}')

last_data = data[-1]
print(last_data)

length_data = len(data)  # ambil panjang data suatu list
print(length_data)

print(f'data sebelum diubah: \n{data}')
data.insert(0, 'guru')
data.insert(1, 'besar')
print(f'data setelah diubah: \n{data}')
data.append('masyaallah')
print(f'data setelah diubah lagi: \n{data}')

new_data = ['ryo', 'dwi', 'rayyan']
data.extend(new_data)
print(f'data gabungan: \n{data}')

# change data
data[3] = 'pipal'
print(f'data setelah diubah: \n{data}')

# remove data
data.remove('masyaallah')
print(f'data setelah 1 data dihapus: \n{data}')

# remove data paling belakang
data.pop()
print(f'data setelah 1 data dihapus lagi: \n{data}')


# Operation data
oper_angka = [1, 2, 5, 6, 6, 6, 5, 4, 7, 8, 3, 4, 2, 1, 0]
oper_angka.count(5)
print(f'\njumlah angka 5 = {oper_angka}')

oper_nama = ['nadya', 'annisa', 'larasati']
index_nadya = oper_nama.index('nadya')
print(f'index nadya = {index_nadya}')

print(f'angka sebelum diurutkan = {oper_angka}')
oper_angka.sort()
print(f'angka sesudah diurutkan = {oper_angka}')
print(f'nama sebelum diurutkan = {oper_nama}')
oper_nama.sort()
print(f'nama sesudah diurutkan = {oper_nama}')
oper_angka.reverse()
oper_nama.reverse()
print(f'angka dan nama setelah di reverse/di sorting by descend = \n{oper_angka}\n{oper_nama}')


# copy list
a = [1, 2, 5, 5, 4, 6]
b = a
print(f'\nini adalah list a : {a}\nini adalah list b : {b}')

a[2] = 4
print(f'(sesudah diganti) \nini adalah list a : {a}\nini adalah list b : {b}')
'''
ketika data satu index didalam salah satu list diganti, maka satu index yang sama pada list lainnya ikut tergantikan
solusi agar tidak terjadi hal spt itu adalah dengan menggunakan method
'''
print(f'\nadress a adalah {hex(id(a))}')
print(f'adress b adalah {hex(id(b))}')

c = a.copy()
print(f'\nadress a adalah {hex(id(a))}')
print(f'adress b adalah {hex(id(b))}')
print(f'adress c adalah {hex(id(c))}')

print(f'\na = {a}')
print(f'b = {b}')
print(f'c = {c}')

c[2] = 3
print(f'\na = {a}')
print(f'b = {b}')
print(f'c = {c}')