# operasi logika dan boolean

# NOT
print("<===NOT===>\n")
a = False
b = not a
print('data a = ', a)
print('-----------NOT')
print('data b = ', b)

# OR
print("\n<===OR===>\n")
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

# AND
print("\n<===AND===>\n")
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

# xor
print("\n<===XOR===>\n")
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)


# latihan komparasi dan logika
print("\n<===Exercise ver 1.0===>")
inputUser = int(input('\nmasukkan angka\nyang kurang dari 3\natau\nlebih dari 10: '))

isKurangDari = (inputUser < 3)
print('Kurang dari 3 =', isKurangDari)

isLebihDari = (inputUser > 10)
print('Lebih dari 10 =', isLebihDari)

isCorrect = isLebihDari or isKurangDari
print('angka yang anda masukkan adalah', isCorrect)

# latihan range 3 to 10 with if else condition
print("\n<===Exercise ver 1.1===>")
inputYuser = int(input('\nmasukkan angka\nyang lebih dari 3\natau\nkurang dari 10: '))

if inputYuser > 0 and inputYuser < 5 :
    print('angka yang anda masukkan', inputYuser, 'dan betul!')
elif inputYuser > 8 and inputYuser < 11 :
    print('angka yang anda masukkan', inputYuser, 'dan benar!')
else :
    print('angka yang anda masukkan tidak masuk ke dalam kategori')

# latihan range 3 to 10 with no if
print("\n<===Exercise ver 1.2===>")
inputOG = int(input('masukkan angka\nyang kurang dari 3\natau\nlebih dari 10: '))

zeroToFive = (inputOG > 0 and inputOG < 5)
eightToEleven = (inputOG > 8 and inputOG < 11)
iskorek = zeroToFive or eightToEleven

print('angka yang anda masukkan adalah', iskorek)