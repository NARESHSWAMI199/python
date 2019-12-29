# class Method:
#     def name(self,a,b):
#         print (a+b)
# m = Method()
# m.name(3,5)

class Smartphone():
    name = "naresh"
    last_name = "swami"
    age = 23
       
    def full_name(self):
        print (f"{self.name}  {self.last_name}")  # if you don't use self then varible can't access in function
        # beacuse you can access the calss var using the class obj

s = Smartphone()



# you can write like that
s.full_name()
#   -------- or -------------
# you can write like that
Smartphone.full_name(s)

