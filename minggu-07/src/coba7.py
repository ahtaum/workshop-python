def f1 (self,x,y):
    return min(x, x+y)

class C:
    f = f1
    def g (self):
        return 'Hallo Dunia'
    h = g