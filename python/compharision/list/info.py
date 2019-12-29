# list compharision

# normally print of these square


# numbers = list(range(1,11))
# new =[]
# for i in numbers:
#     new.append(i**2)
# print(new)


# using list compharsion print of these square

# squares = [i**2 for i in range(1,11)]
# print(squares)



# normally print of these nagative

# numbers = [1,2,3,4]
# new = []
# for i in numbers:
#     new.append(-i)
# print(new)


# using list compharsion print of these nagative

# numbers = [-i for i in range(1,5)]
# print (numbers)


# create a new list with names first charactor
# names = ["naresh" ,"manish" , "swami"]
# useing names create like this
# new = ["n","m","s"]

# normally


# new = []
# for name in names:
#     new.append(name[0])
# print(new)


# using compharsioion

names = ["naresh" ,"manish" , "swami"]
new = [i[0] for i in names]
print(new)