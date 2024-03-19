def helloWorld():
    print(f'Hello putriirans,')
    print(f'yang anggun sekali,')
    print(f'nan lucu sekali,')
    print(f'hehe becanda aja sie')


helloWorld()

print(f'\n')

# function with argument/parameter


def bismillah(name):
    print(f'semoga harimu selalu menyenangkan {name}')


bismillah("putriirans")

print(f'\n')

def operation(num1, num2):
    value = (num1 + num2)*2
    print(f'hasil dari pengoperasian angka {num1} dan {num2} = {value}')

operation(5, 4)

print(f'\n')

def peserta_utbk(kader_utbk):
    data_peserta = kader_utbk.copy()
    data_peserta.append("galih")
    for i, peserta in enumerate(data_peserta):
        print(f'peserta ke-{i+1} : {peserta}')

list_tfs = ["bagas", "naufal", "hisyam", "raffi"]
peserta_utbk(list_tfs)

print(f'\n')

def kuadrat(n):
    '''function with return value'''
    value = n**2
    return value

x = kuadrat(7)
print(x)

print(f'\n')

def tambah_baru(ang1,ang2):
    return ang1+ang2

baru = tambah_baru(100,250)
print(baru)