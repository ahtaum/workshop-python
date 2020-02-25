# def parrot(voltage, state='a stiff', action='voom'):
#      print("-- This parrot wouldn't", action, end=' ')
#      print("if you put", voltage, "volts through it.", end=' ')
#      print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print (f(0))