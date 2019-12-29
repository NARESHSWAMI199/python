

# here we self make a function wich takes a function and give output

# here we first check a example

# let's find the square of the list

list1= [1,2,3,4,5]
print(list(map(lambda a : a**2, list1)))


# now we make function wich takes a function in a functions

def my_map(func, l):
    new = []
    for i in l:
        new.append(func(i))
    return new

print(my_map(lambda a :a**2,list1))

# using  list compharision

def l_map(func , l):
    return [func(i) for i in l]
print(l_map(lambda a: a**3 , list1))


# how to my_map function
# step 1 take a func and l
# step 2 unpack the l
# append the value in new l with passing in func
# func will return square of i 
# and the my_map() will return new list
# and the new list is also have the square of the numbers