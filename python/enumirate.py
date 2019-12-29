

# we will print value or his index in a list

list1 = ["naresh" ,"swami","kaliya"]

# pos = 0

# for i in list1:
#     print(f"{pos} index : name is  {i}")
#     pos+=1



# using enumerate function

# for pos , name in enumerate(list1):
#     print(f"{pos} index : name is  {name}")


# finding the index of the  "swami" in list1 using enumerate

for i,name in enumerate(list1):
    if name == "swami":
        print (i)

