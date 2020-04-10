import reprlib
import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta','yellow'], 'blue']]]
print (" Karater yang dipakai : ", reprlib.repr(set('judith'))) # berfungsi untuk membaca karater apa saja yg dipakai untuk membuat string tsb
print ("hasilnya : ", pprint.pprint(t, width=30))