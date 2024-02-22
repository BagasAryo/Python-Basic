# LOOPING LIST DAN ENUMERATE

# FOR LOOP
print(f'FOR LOOP')
data = [1, 6, 5, 7, 3, 2]

for i in data:
    print(f'angka = {i}')


# FOR LOOP AND RANGE
print(f'\nFOR LOOP DAN RANGE')
nama = ['bagas', 'aryo', 'priyatama', 'ortega']
length = len(nama)

for i in range(length):
    print(f'nama = {nama[i]}')


# WHILE LOOP
print(f'\nWHILE LOOP')
angka = [10, 9, 5, 11, 12]
panjang = len(angka)
j = 0
while j < panjang:
    print(f'angka while = {angka[j]}')
    j += 1


# LIST COMPREHENSION
print(f'\nLIST COMPREHENSION')
data = ['jenna', 2, 3, 7, 'ortega']

[print(f'data = {i}') for i in data]

data = [2, 3, 7]
data_kuadrat = [i**2 for i in data]
print(f'ini adalah kuadrat = {data_kuadrat}')

# ENUMERATE
print(f'\nENUMERATE')
datalist = ['maxine', 1, 2, 5, 'mad']
for i,a in enumerate(datalist): # first variable was for index whereas second variable was for the data contain list
    print(f'data ke-{i} : {a}')