

# the map functions basic functionlaty is that this take two args , fist is function and secound is the list 



def add(a):
    return a**2

list1 = [2,3,4]
# print(add(list1))  # error this will return beacuse don't return of a list square

# new =list(map(add,list1))  # this will unpaked the list or tuple as pass in function

# print(new)


# you can simply like this 

new1 = list(map(lambda a: a**2 , list1 ))
print(new1)



