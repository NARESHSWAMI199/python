

def decorator(func):
    def wapper(*args, **kwargs):
        print("this is a awsome function ")
        return func(*args,**kwargs)
# also use return here beacuse some function will return something

# work procces of decoreater
# func = decoretor(func)  # here the decorder function call the wapperfunction and pass in your func name variale 
# when you call func then you are calling wapper function
    return wapper



# if you pass any perameter with your function then also pass perameter in your wapper function so 
# we use the *args **kwargs with wapper function
@decorator
def func (a):
    print(f"this function take a value this is {a}")

func(4)



# one more function this will return 

# if your function will then also return a function
@ decorator
def add(a,b):
    return a+b
print(add(2,3))