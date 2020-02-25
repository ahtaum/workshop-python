knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

for i, v in enumerate(['tic','tac','toe']):
    print(i, v)

pertanyaan = ['name','Quest','favorite colour']
jawaban = ['lancelot','cawan soeci','biru']
for q, a in zip(pertanyaan, jawaban):
    print('what is your {0}? it is {1}.'.format(q,a))

for i in reversed(range(1,10,2)):
    print(i)

basket = ['apel', 'orange', 'apel', 'pear', 'orange', 'pisang']
for f in sorted(set(basket)):
    print(f)