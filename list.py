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
print(data)

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