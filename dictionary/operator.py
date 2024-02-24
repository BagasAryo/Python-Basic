# operator dictionary

data_dict = {
    'first': "hana",
    'second': 'aulia',
    'third': 'putri'
}

# panjang dictionary
LENDICT = len(data_dict)
print(f'panjang dictionary: {LENDICT}')

# checking apakah key exist or no
KEY = 'second'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict: {CHECKKEY}')

# mengakses value (read) dengan get()
# ketika tidak pakai get dan key nya salah akan terjadi error
print(data_dict['first'])
print(data_dict.get('first'))
# cek menggunakan custom message
print(data_dict.get('fourth', 'tidak ditemukan'))

# mengupdate data
data_dict['first'] = 'hanaas' # mengupdate a.k.a mengedit data yang sudah ada
print(data_dict)
data_dict['fourth'] = 'sadie' # menambahkan data yang belum ada di dictionary
print(data_dict)

data_dict.update({'first':'hanabule'}) # mengupdate/menambahkan data menggunakan method
print(data_dict)
data_dict.update({'fifth':'sink'})
print(data_dict)

# delete data
del data_dict['third']
print(data_dict)
