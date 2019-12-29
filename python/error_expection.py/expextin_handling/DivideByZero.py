
a = int(input())
b = int(input())



def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        print("sorry can't divide by zero")
    except TypeError:
        print("check the value type is not a int")
   
print(divide(a,b))
