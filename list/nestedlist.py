data0 = [1, 2]
data1 = [5, 6]
commonlist = [1, 2, 3, 4, 5, 6]

print(f'list biasa = {commonlist}')

list2D = [data0, data1, 5, 6]

print(f'list 2D = {list2D}\n')

# implementation w for

member1 = ['azizi', 22, 'ancika']
member2 = ['amanda', 21, 'frix']
member3 = ['greesel', 18, 'icel']

member = [member1, member2, member3]

for i in member:
    print(f'Nama : {i[0]}')
    print(f'Umur : {i[1]}')
    print(f'Nama lain : {i[2]}\n')

# by reference
membercopy = member.copy()
print(f'membercopy = {membercopy}')
member1[0] = 'marsha'
print(f'membercopy = {membercopy}')
print(f'member = {member}')