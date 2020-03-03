import math
print (f'the value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}') # name:10 buat panjang kolom

binatang = 'eels'
print (f'My hovercraft is full of {binatang}.')
print (f'My hovercraft is full of {binatang!r}.')