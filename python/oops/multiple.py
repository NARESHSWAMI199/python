class A:
    def class_a_method(self):
        print ("this method called by class a")
    def hello(self):
        print("this is class A")
class B:
    def class_b_method(self):
        print ("this method called by class B")
    def hello(self):
        print("this is class B")

class C (B,A):   # you can access here any fuction according sequance 
    pass

instance_a = C ()
instance_a.hello()  
# print(help(instance_a))

# use mro method for same help  but this will give a list
print(C.mro())
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>] like this