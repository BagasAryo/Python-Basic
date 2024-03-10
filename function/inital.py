def helloWorld():
    print(f'Hello putriirans,')
    print(f'yang anggun sekali,')
    print(f'nan lucu sekali,')
    print(f'hehe becanda aja sie')

helloWorld()

print(f'\n')

#function with argument/parameter 

def bismillah(name):
    print(f'semoga harimu selalu menyenangkan {name}')

bismillah("putriirans")

def operation(num1, num2):
    value = (num1 + num2)*2
    print(f'hasil dari pengoperasian angka {num1} dan {num2} = {value}')

operation(5,4)

print(f'\n')

def peserta_utbk(kader_utbk):
    data_peserta = kader_utbk.copy()
    data_peserta.append("galih")
    for i,peserta in enumerate(data_peserta):
        print(f'peserta ke-{i+1} : {peserta}')

list_tfs = ["bagas", "naufal", "hisyam", "raffi"]
peserta_utbk(list_tfs)