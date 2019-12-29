
#  here the star opreater take many item as arguments and return a tuple


# def funcname(*args):
#     print(args)
#     print(type(args))

# funcname(1,3,4,5,6)

# (1, 3, 4, 5, 6)
# <class 'tuple'>


# here the main work of * opreator on args place you can write every thing without space

def funcname(*args):
    total = 0
    for i in args:
        total+= i
    return total


print(funcname(1,2,3,4))
