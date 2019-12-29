
# we have in return_func_func.py

def to_power(x):
    def value(a):
        return a**x
    return value

var = to_power(3)
print(var(3))
