# width and multiline
name = 'jenna ortega cantik banget'
age = 22
height = 160.3
shoeSize = 35

print(5 * '-' + 'STANDARD' + 5 * '-')
data = f'nama : {name}, umur : {age}, tinggi badan : {height}, ukuran sepatu : {shoeSize}'
print(data)

# newline using \n
print('\n' + 5 * '-' + 'USING \\n' + 5 * '-')
data = f'nama : {name}\numur : {age}\ntinggi badan : {height}\nukuran sepatu : {shoeSize}'
print(data)

# newline using triplets
print('\n' + 5 * '-' + 'STANDARD' + 5 * '-')
data = f'''nama          : {name},
umur          : {age},
tinggi badan  : {height},
ukuran sepatu : {shoeSize}
'''
print(data)