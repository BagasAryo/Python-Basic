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
inputUser = int(input('\nmasukkan angka\nyang kurang dari 3\natau\nlebih dari 10: '))

isKurangDari = (inputUser < 3)
print('Kurang dari 3 =', isKurangDari)

isLebihDari = (inputUser > 10)
print('Lebih dari 10 =', isLebihDari)