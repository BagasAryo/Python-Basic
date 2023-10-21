confirm = input('ya/tidak? ')

while confirm == 'ya' :

    a = float(input('Masukkan x1 : '))
    b = float(input('Masukkan x2 : '))
    c = float(input('Masukkan y1 : '))
    d = float(input('Masukkan y2 : '))

    y = float(d - c)
    x = float(b - a)

    if y == 0 :
        print('Garis tersebut merupakan garis horizontal')
    else :
        if x == 0 : 
            print('Garis tersebut merupakan garis vertikal')
        else :
            z = float(y / x)
            print('Garis tersebut memiliki gradien', z)