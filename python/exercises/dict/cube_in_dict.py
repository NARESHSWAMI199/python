

value = int(input("enter the value : "))

def cube(a):
    new = {}
    for i in range(1,a+1):
        new[i] = i**3
    return new
print (cube(value))
        