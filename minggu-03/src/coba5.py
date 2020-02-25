vec = [-4, -2, 0, 4]
lurr = [x*2 for x in vec]
print (lurr)

lurr = [x for x in vec if x >= 0]
print(lurr)

lurr = [abs(x) for x in vec]
print (lurr)

buahsegar = ['pisang','loganberry','buah passion ']
print (buahsegar)

tupel = [(x, x**2) for x in range(6)]
print (tupel)

vec = [[1,2,3],[4,5,6],[7,8,9]]
print ([num for elem in vec for num in elem])
