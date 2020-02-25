basket = {'apple','orange','apple','pear','orange','banana'}
print (basket)
print ('orange' in basket)
print ('crabgrass' in basket)

a = set('abrakadabra')
b = set('alacazam')
print (a)

print (a - b)
print (a | b)
print (a & b)
print (a ^ b)

a = {x for x in 'abrakadabra' if x not in 'abc'}
print (a)