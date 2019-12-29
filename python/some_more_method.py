
# formkeys
# names = dict.fromkeys(["name","age"],"unkown")
# print (names)


# get method 

Info = {"name":"naresh" ,"surname":"swami"}
# print(Info["name"])
# print (Info.get("name"))

# print(Info["names"])  # key error
# print (Info.get("names")) # None
# print (Info.get("names" , not found)) # not found


# clear dict 

# Info.clear()
# print(Info) # output  {}


# copy 
d = Info.copy()  # this is not orignal dict only a copy
d.pop("name")  
print (d)
print(Info)

