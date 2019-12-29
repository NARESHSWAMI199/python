value = input("enter your name  or a string : ")
def count(a):
    name = {}
    for i in a:
        name[i] = a.count(i) 
    return name

print(count(value))
