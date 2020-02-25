# buat fungsi bilangan Fibbonaci
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end='')
        a,b = b, a+b
    print()

# panggil fungsi

fib(2000) # panggil fungsi dengan cara sederhana

# panggil fungsi dengan membuat variabel mendeklarasikan sebagai fungsi
# f = fib
# f(100)