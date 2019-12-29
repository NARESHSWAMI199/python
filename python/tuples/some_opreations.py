
# looping in tuples
# tuples with one element
# tuples whitout parenthisis
# tuples unpacking
# list inside tuples
# some functions that you can use with tuples



#looping

# names = ("nareh",4,"swami")
# for i in names:
#     print(i)

# tuple with one element

# names = ("swami") # this is not tuple  <class 'str'>
# names = ("swami",)# this is tuple beacuse tuple has must two vlaue or one comma  <class 'tuple'>
# print(type(names))

# tuple without parenthisis

# names = "naresh", 4,5,"swami"   <class 'tuple'>
# print(type(names))

#unpacking

# names = ("naresh" ,"swami",)
# name1, name2 = names
# print(f"{name1} , {name2} ,{names}")

# list inside tuples

# n = (1,3,4,[1,3,4,"naresh"])
# print(n[3].pop()) # like append , pop(1), insert(),extends(), and many more fuction wich you can perform with list 
# print(n)


# some function we cam use with tuples

# min , max ,min 

num = 1,2,3,4
print(sum(num))
print(max(num) , min(num))