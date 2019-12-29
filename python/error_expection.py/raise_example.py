class Phone:
    def __init__(self,name):
        self.name = name


class Smartphome:
    def __init__(self):
        self.list = []
 
    def add_item(self,item):
        if isinstance(item,Phone):
            self.list.append(item)
            return self.list
        else :
            raise  TypeError("the instance should be smartphone class")
        
s = Smartphome()
p = Phone("sumsung")
print(s.add_item(p))