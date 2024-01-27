print('\nKONVERSI SUHU')

cel = float(input("masukkan nilai celcius : "))

# konversi celcius ke reamur

reamur = float(4/5*cel)

print("nilai konversi celcius ke reamur adalah: ", reamur, "reamur")

# konversi celcius ke fahrenheit

fahren = float(9/5*cel+32)

print("nilai konversi celcius ke reamur adalah: ", fahren, "fahrenheit")

# konversi fahrenheit ke kelvin

Fahre2 = float(input('masukkan nilai fahrenheit: '))

convFahre = float((5/9 * (Fahre2 - 32)) + 273)

print('nilai konversi fahrenheit ke kelvin adalah: ', convFahre, 'kelvin')

# konversi kelvin ke fahrenheit

Kelvin2 = float(input('masukkan nilai kelvin: '))

convKelv = float(9/5 * (Kelvin2 - 273) + 32 )

print("nilai konversi kelvin ke fahrenheit adalah: ", convKelv, "fahrenheit\n")