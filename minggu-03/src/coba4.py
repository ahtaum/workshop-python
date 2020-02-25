squares = []
for x in range(10):
    squares.append(x**2)

print (squares)

combs = []
for x in [1,2,3]:
    for y in [3,1,3]:
        if x != y:
            combs.append((x,y))

print (combs)
