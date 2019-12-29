class Smartphone:
    price = 40000
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def discount(self,price):
        return self.price - (price/100)*self.price

s = Smartphone("sumsung","30rt")
s.price = 2000  # you can change the condition according object using self key word in method before price
print(s.discount(10))