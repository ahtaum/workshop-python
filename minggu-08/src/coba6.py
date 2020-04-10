from datetime import date

now = date.today()
tanggallahir = date(1999, 6, 8)
umur = now - tanggallahir
print (umur.days)