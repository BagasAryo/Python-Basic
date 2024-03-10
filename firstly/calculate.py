# ordinary calculator

angka1 = float(input('masukkan angka pertama anda: '))
oper = input('pilih operator(+, -, x, /): ')
angka2 = float(input('masukkan angka kedua anda: '))

if oper == '+' :
    hasil = angka1 + angka2
elif oper == '-' :
    hasil = angka1 - angka2
elif oper == 'x' :
    hasil = angka1 * angka2
elif oper == '/' :
    hasil = angka1 / angka2

print(f'hasilnya adalah: {hasil:.1f}')