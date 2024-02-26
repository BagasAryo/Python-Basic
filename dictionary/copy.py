# copy dictionary

bala2 = {
    'luch': 'aldean tegar',
    'hyde': 'ade setiawan',
    'ghost': 'mada rahadian',
    'aninbisnis': 'aninditha cahyadi',
    'meentut': 'anastasia yasmeen'
}

streamer = bala2.copy()

print(f'1. bala-bala = {bala2}\n')
print(f'1. streamer {streamer}\n')

bala2['aninbisnis'] = 'aninjkt48'
print(f'2. bala-bala = {bala2}\n')
print(f'2. streamer {streamer}\n')

# pop dictionary (berdasarkan key)
data_luch = streamer.pop('luch')
print(f'3. bala-bala = {bala2}\n')
print(f'3. streamer {streamer}\n')

# popitem dictionary (berdasarkan item yang terakhir)
data_terakhir = streamer.popitem()
print(f'4. data terakhir = {data_terakhir}\n')
print(f'4. streamer {streamer}\n')
