from copy import deepcopy
data0 = [1, 2]
data1 = [3, 4]

listdata = [data0, data1]

print(f'list data = {listdata}')

listdata_copy = listdata.copy()
print(f'list copy = {listdata_copy}\n')

listdata[0] = [5, 6]
data1[0] = 10

print(f'adress asli = {hex(id(listdata))}')
print(f'adress copy = {hex(id(listdata_copy))}\n')
print(f'adress mem asli = {hex(id(listdata[0]))}')
print(f'adress mem copy = {hex(id(listdata_copy[0]))}\n')

print(f'list data = {listdata}')
print(f'list copy = {listdata_copy}')


data2 = [10, 15]
data3 = [20, 30]
listdatadeep = [data2, data3]
listdatadeep_copy = deepcopy(listdatadeep)

listdatadeep[1] = [5, 6]
data2[0] = 100

print(f'adress asli = {hex(id(listdatadeep))}')
print(f'adress copy = {hex(id(listdatadeep_copy))}\n')
print(f'adress mem asli = {hex(id(listdatadeep[0]))}')
print(f'adress mem copy = {hex(id(listdatadeep_copy[0]))}\n')

print(f'list data = {listdatadeep}')
print(f'list copy = {listdatadeep_copy}')
