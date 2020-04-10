import locale

print (locale.setlocale(locale.LC_ALL, 'English_United States.1252'))

conv = locale.localeconv()
x = 1234567.8
print (locale.format_string("%d", x, grouping=True))