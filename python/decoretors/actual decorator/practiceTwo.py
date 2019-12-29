from functools import wraps

# def dec (function):
#     @wraps(function)
#     def wrapper(*args ,**kwargs):
#         new = []
#         for i in args:
#             new.append(type(i) == int)
#         if all(new):
#             return function(*args,**kwargs)
#         else:
#             print("sorry this is not a valid input")
#     return wrapper

# @dec
# def add(a,b):
#     return a+b

# print(add(3,[34]))


# using compharision
def dec (function):
    @wraps(function)
    def wrapper(*args ,**kwargs):
        if all([type(arg)==int for arg in args]):
            return function(*args,**kwargs)
        else :
            print ("invalid")
    return wrapper

@dec
def add(a,b):
    return a+b

print(add(3,[34]))