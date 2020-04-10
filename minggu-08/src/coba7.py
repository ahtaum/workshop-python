import zlib

s = b'tydac ada yang aman'
print (len(s)) # menghitung jumlah karakter pada variabel s

t = zlib.compress(s) # mengkompress agar jumlah karakter pada variabel s menjadi lebih kecil ukurannya
print (len(t))

print (zlib.decompress(t)) # mengdekompress variabel yang sebelumnya dikompress atau di exstrak
print (zlib.crc32(s))