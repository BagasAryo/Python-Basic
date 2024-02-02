# operasi dan manipulasi string

# 1. menyambung string (concatenate)
first_name = "Mang"
mid_name = "Ujang"
last_name = "Bongah"

complete = first_name + ' ' + mid_name + ' ' + last_name
print(complete)

# 2. menghitung panjang string
length = len(complete)
print('the length is ' + str(length))

# 3. operator untuk string

# 3.1 check apakah ada char atau string di dalam sebuah string

x = "Ujang"
check = x in complete
print('apakah ada char/string ' + x +
      ' di dalam kalimat ' + complete + ' ? ' + str(check))

x = "Ujang"
check = x not in complete
print('apakah tidak ada char/string ' + x +
      ' di dalam kalimat ' + complete + ' ? ' + str(check))

# indexing
print('\nindex ke-0:', complete[0])
print('index ke-1:', complete[2])
print('index ke-[3:8]:', complete[3:8])
print('index ke-[3,5,7,9]:', complete[3:10:2])

# decimal paling kecil dan besar
print('paling kecil: ' + min(complete))
print('paling besar: ' + max(complete))

ascii_code = ord(" ")
print('ASCII code untuk spasi adalah: ' + str(ascii_code))
data = 111
print('ASCII code untuk spasi adalah: ' + chr(data))

# 4. operator dalam bentuk method

name = 'Oding koroding kiding'
jumlah = name.count('n')
print('jumlah n pada', name, 'adalah', jumlah)

# part 2

# merubah case dari string
nama = 'bagas aryo priyatama'
print('namaku: ' + nama.upper())
print('namaku: ' + nama.capitalize())

# pengecekan isX
buah = 'MANGGA'
shall_buah = buah.isupper()
print(buah + ' = ' + str(shall_buah))

pengecekanLangsung = 'Vortex Series Xera'.startswith('Vortex')
print('startwith = ' + str(pengecekanLangsung))
pengecekanLangsung = 'Vortex Series Xera'.endswith('xera')
print('endswith = ' + str(pengecekanLangsung))

# penggabungan dan pemisahan / join dan split
keyb = ['fantech', 'maxfit', 'bagus']
gabung = ' - '.join(keyb)
print(keyb)
print(gabung)

mouse = 'noir m1 lite'
pisah = mouse.split(' ')
print(pisah)
print(mouse)

# allocation character rjust() ljust() center()
kanan = 'kananbang'.rjust(10)
print('\'' + kanan + '\'')

kiri = 'kiribang'.ljust(10)
print('\'' + kiri + '\'')

tengah = 'tengahbang'.center(12, '=')
print('\'' + tengah + '\'')

# kebalikannya - strip
kiri = kiri.strip()
print('\'' + kiri + '\'')

tengah = tengah.strip('=')
print('\'' + tengah + '\'')