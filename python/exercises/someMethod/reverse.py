
names = ["naresh", "swami"]

# name = ["naresh", "swami"]
def funcname(l,**kwargs):
    if kwargs.get("reverse_str") == True:
        return [n[::-1].title() for n in l ]
    else:
        return [name.title() for name in l ]
       
print(funcname(names,reverse_str = True))