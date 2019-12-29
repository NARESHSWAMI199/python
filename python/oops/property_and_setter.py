class mobile:
    def __init__(self,name,modal,price):
        self.name = name
        self.modal = modal
        self._price = max(price,0)
    @property   # work as a getter 
    def price(self):
        return  self._price 
    
    @price.setter # work as a sette
    def price (self, new):
        self._price = max(new,0)
       

m = mobile("nokia","110",45)
m.price = 500
print(m.price)