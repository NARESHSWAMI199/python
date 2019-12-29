
from functools import wraps

def decorator(func):
    @wraps(func)
    def warpper(*args, **kwargs):  # this args take as a tuple 
        ''' this is a warpper function'''
        print("this is a awsome function ")
        return func( *args,**kwargs)  
# also use return here beacuse some function will return something

# work procces of decoreater
# func = decoretor(func)  # here the decorder function call the wapperfunction and pass in your func name variale 
# when you call func then you are calling wapper function
    return warpper


@ decorator
def add(a,b):
    '''this is add function'''
    return a+b
print(add(2,3))



# if you check the name of your add function and print your functions doc string then you get the 

# name is wrapper function and the doc also will wrapper function for solve this problem we imort wraps
print(add.__doc__)
print(add.__name__)