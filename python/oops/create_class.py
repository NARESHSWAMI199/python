class Mobile:
    def __init__(self,name,price):
        print ("this is a cons")
        self.name = name
        self.price = price
        self.fulldeatil = name + str(price)
m = Mobile("sumsung",243)
print(m.fulldeatil)