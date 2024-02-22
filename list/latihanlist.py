# program list buku

kumpulan_buku = []

tanya = 'y'
while tanya == 'y':
    print(f'Data Buku')
    writer = input(f'Masukkan Nama Penulis\t\t: ')
    title = input(f'Masukkan Judul Buku\t\t: ')

    buku_baru = [writer, title]
    kumpulan_buku.append(buku_baru)

    tanya = input(f'apakah ingin dilanjutkan?')

for i, buku in enumerate(kumpulan_buku):
    print(f'buku ke-{i+1}:\n penulis : {buku[0]} | judul : {buku[1]}')
