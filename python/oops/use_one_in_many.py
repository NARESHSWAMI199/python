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

class Smartphone2(Phone):
    def __init__(self, name,modal,price,camera,ram,rear,memory):
        super().__init__(name,modal,price)
        self.camera = camera
        self.ram = ram
        self.rear = rear
        self.memory = memory


s = Smartphone('oneplus','6',60000,'45',4) 
m = Phone("nokia",'1100',700)
s2  = Smartphone2('sumsung','k9',40000,'45px',4,'20px',30)
print (s2.name)
print(s.full_detail())
print (m.name)
