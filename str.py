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
print('apakah ada char/string ' + x + ' di dalam kalimat ' + complete + ' ? ' + str(check))

x = "Ujang"
check = x not in complete
print('apakah tidak ada char/string ' + x + ' di dalam kalimat ' + complete + ' ? ' + str(check))

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