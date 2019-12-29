

# Q what is dict ?
# A  dict is a unordered pair of data with his key

# dict are muitable we can changes in this
# don't store repetative vlaue


# you don't have index in dict

information  = {"name" : "naresh" , "age" : 24 }
# you can sore anything in dict
print(information)
print(type(information))

# add some value in the empty dict
names  = {}
names["name"] = "naresh"
names["age"] = 24
names['age'] = 45
print(names)


# how to access value from dict

#print(names["naresh"])  # key error the second side value is not a key
print(names["name"])


# some data in dict

items = {
    
    "item":{"naresh"},  # key must a stinb or integer
    "name":"naresh",
    5 : "manish"
}

print(items[5])