class coba5:

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick (self,trick):
        self.tricks.append(trick)

d = coba5('Fido')
e = coba5('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print (d.tricks)
print (e.tricks)