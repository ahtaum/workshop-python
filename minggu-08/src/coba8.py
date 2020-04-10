from timeit import Timer

timer = Timer('t=a; a=b; b=t', 'a=1; b=2').timeit() # menset timer
print (timer)