
# normally if we print dict't square then do like this
# square = {}
# for i in range(1,6):
#     square[i] = i**2

# print (square)


# using list compharision

# new = { i:i**2 for i in range(1,6) }
# print(new)
# print (type(new))


# new = { f"square of {i}":i**2 for i in range(1,6) }
# print(new)
# print (type(new))


# we count the char in dict 
# normally


items = input("enter your name : ")

# new = {}
# for i in items:
#     new[i] = items.count(i)

# print(new)


# using dict compharsion

new = {i:items.count(i) for i in items}
print(new)