

# let's start


# here like list , string ,tuples , sets ... are iterable

# and when we use for loop in list or tuple or string then the for loop call the iter funtion and pass the list in iter
# and next this will call next() function this will return your list element


# like 

numbers = [1,2,3,4]
number = iter(numbers)
# print(next(number))
# print(next(number))
# print(next(number))
# print(next(number))

print (number) #  <list_iterator object at 0x7f158fa40110>  return like this
# simple mean of this the for loop convert the list in obeject and run the next() method



# but the map function is a object right  then how we can for in this

square = map(lambda a: a**2, numbers)

print(square) # this return like this   <map object at 0x7f8be8c7bf10>

# but we can use for loop with him  

# let's understand how work this   

# print(next(square))
# print(next(square))


#  so we call the map is a iterator