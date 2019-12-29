

# if you use the one more permater before *args then your arguments's first value will go on your new perameter

def multiply(a,*args):
    mul = 1
    print(f" args is {args} and a is {a}")
    for i in args:
        mul *= i 
    return mul


print(multiply(2,3,4))


# here the first argument go on "a" and next vlaue go on *args and this will return a tuple

# this is output   


# args is (3, 4) and a is 2
#12