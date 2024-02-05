print('==BEFORE==')
name = 'janne ortega'
str = 'hello ' + name
print(str)

# string w format
print('==AFTER==')
nama = 'enid sinclair'
format_strr = f'nama = {nama}'

# bilangan bulat
angka = 22000
format_strr = f'angka = {angka}'
format_strr = f'angka tanpa koma = {angka:,} dan menggunakan koma = {angka}'
print(format_strr)

# bilangan desimal
desimal = 45.99021
format_strr = f'angka desimal = {desimal:.0f}'
print(format_strr)

# plus - minus
plus = 5
minus = -5
format_strr = f'angka plus = {plus:+d} dan angka minus = {minus:+d}'
print(format_strr)

# format persen
persen = 0.5778
format_persen = f'persentase = {persen:.2%}'
print(format_persen)

# operasi aritmatika
hrg = 10000
jml = 4

format_total = f'total harga = Rp.{hrg*jml:,}'
print(format_total)

# format binary octal hexadecimal
angka = 255
format_binary = f'angka ke binary = {bin(angka)}\n'
format_octal = f'angka ke octal = {oct(angka)}\n'
format_hexa = f'angka ke hexa = {hex(angka)}\n'

print(format_binary, format_octal, format_hexa)