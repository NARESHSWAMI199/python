class Persion:
    count = 0
    def __init__(self):
        Persion.count +=1  # here don't use self before count because the per object create new count var 
        # so we use Class name


    # if you want make a class method then use a decorator
    @classmethod
    def display(cls):
        print (f"{cls.count} {cls.__name__}")

    # def count_obj(self):
    #     print (self.count)
              
p = Persion()
p1 = Persion()
p2 = Persion()
p.display()

# class variable is same for every object
# but object variable are seprated