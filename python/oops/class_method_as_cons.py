class Persion:

    def __init__(self,name,last_name,age):
        self.name = name
        self.last_name = last_name
        self.age = age

    @staticmethod
    def hello():
        print ("hello i am naresh swami")
    

    @classmethod
    def full_string(cls,string):
        name,last_name,age = string.split(',')
        # print (f"{name} {last_name} {age}")
        return cls(name,last_name,age)

p = Persion("naresh","swami",32)
p1 =  Persion.full_string('naresh,swami,24')
print (p1.name)
Persion.hello()

# _name   some thing like method are a conventions show for that this is a private method
# __name__ these type method we call the dudel method or encapsulation method