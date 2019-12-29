

# def avrage_finder (*args):
#     print (*args)
#     new1 = []
#     for i in zip(*args):
#         new1.append((sum(i)/len(i)))
#     return new1
# print(avrage_finder([1,2,3],[4,5,6]))



#   in one line

list1 = [1,2,3]
list2 =[4,5,6]
# new = lambda *args: [(sum(i)/len(i)) for i in zip(*args)]
# print(new(list1,list2))


# how this is working first we pass two list and *args take a tuple or and we for run for loop in tuple the we don't
# run nasted so we upacking the tuple that have two lists and and when we use with zip function then that make a 
# tuple of 1 char of lists  and we run for loop for get itrator values and they are also tuple. then sum(tuple)/len(tuple)


# def dislay(*args):
#     new  = list(zip(*args))
#     print(new)
# dislay(list1,list2)

# here args take list and give tuple



# print (len((1,2,3,4))) 

# a len function and sum function can work with tuple