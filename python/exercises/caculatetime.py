import time 
from functools import wraps

def calculate_time(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        t1 = time.time()
        va =  func(*args,**kwargs)
        t2 =time.time()
        print(f"{t2-t1} take time in run")
        return va
    return wrapper


@calculate_time    
def add(a,b):
    return a+b

print(add(2,3))
