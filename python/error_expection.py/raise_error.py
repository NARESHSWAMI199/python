class Animal:
    def __init__(self,name):
        self.name = name
    def sound (self):
        raise NotImplementedError("sorry must implement sound mehod in your class")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "bhow bhow"


Doggy = Dog('Dog',"pug")
print (Doggy.sound())