for n in range(2, 10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'sama dengan',x, '*', n//x)
            break
    else:
        print(n, 'adalah sebuah nomor primer')