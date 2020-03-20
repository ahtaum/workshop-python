class coba8:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update = update

class coba8SubClass(coba8):  # class turunan dari class coba8
    def update(self,keys,values):
        for item in zip(keys, values):
            self.items_list.append(item)
