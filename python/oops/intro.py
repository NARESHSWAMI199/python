class Persion:
    def __init__(self,name,last_name,age):
        print ("this a constructor or Init function")
        self.first_name = name
        self.last_name = last_name
        self.age = age
        

# here the self represent the object 

p1 = Persion("naresh","swami",24)

        
# if write like  print(p1.name) this then
# AttributeError: 'Persion' object has no attribute 'name'

# if you don't use self then         
# AttributeError: 'Persion' object has no attribute 'name'