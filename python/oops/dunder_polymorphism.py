class Phone:
    def __init__ (self,name,price,model):
        self.name = name
        self.price = price
        self.model = model

#   the __str__ method use for print the object like " toString in java  and auto called"
    def __str__(self):
        return f" name {self.name} price {self.price} model {self.model}"   # the __str__ method always return 
#  __repr__ method is use for print the object but use Debuging time and auto called
    def __repr__(self):
        return  f" name {self.name} price {self.price} "


 # this is use for opreater overloading __add__ , __mul__ ,__divid__ 
    def __add__  (self,other):
        return self.price + self.price
 
p1 = Phone("nokia",34000,"nok 8 ")
p2 =  Phone("sumsung",40000,"sumsung 8 ")
print(p1+p2)   # Here the plus singn represent the overloding and polymorephism
# print(str(p1))
# print(repr(p1))   



# method method overriding is a condition to repersernt the polymorphism
# and you can say polymorephism is a two form of any opreator object and method