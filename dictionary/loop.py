# looping for dictionary

poisons = {
    'putri': 'putriirans',
    'hana': 'hanaauliap',
    'hmqm': 'shariyahcrilley',
    'rae': 'rachel',
    'wednesday': 'jennaortega',
    'max': 'sadiesink',
}

for poison in poisons:
    print(poison)  # yang keluar adalah key nya

# operator untuk mengambil item / iterable
key = poisons.keys()
print(key)  # menampilkan dictionary key nya

# print('\n')
for key in poisons.keys():
    print(poisons.get(key))  # menampilkan value berdasarkan key nya
# print('\n')

value = poisons.values()
print(value)  # menampilkan dictionary value nya

for value in poisons.values():
    print(value)  # menampilkan value

print('\nmenggunakan get()')
for value in poisons:
    print(poisons.get(value))  # menampilkan value

item = poisons.items()
print(item)

for item in poisons.items():
    print(item)

for key, value in poisons.items():
    print(f'key : {key}, value : {value}')