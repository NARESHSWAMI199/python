class Phone:
    def __init__(self,name,modal,price):
        self.name = name
        self.modal = modal
        self.price = price

    def full_detail(self):
        return f"{self.name}   {self.price}  {self.modal}"

    def price(self):
        print (self.price)

class Smartphone(Phone):
    def __init__(self,name,modal,price,camera,ram): 
        super().__init__(name,modal,price)   # this will give the permission using the attributes in Smartphone
        # or auto create object instance for the subclass or derived class  
        self.camera = camera
        self.ram = ram


s = Smartphone('oneplus','6',60000,'45',4) 
m = Phone("nokia",'1100',700)
print(s.full_detail())
print (m.name)