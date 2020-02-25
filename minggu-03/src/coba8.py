a = [-1,1, 66.25, 333, 333, 1234.5]
del a[0] # hapus di indexs ke 0 dari list a
print (a)

del a[2:4] # hapus dari index ke 2 sampe ke 4 tapi index ke 4 tidak terhapus
print (a)

del a[:]
print (a)