numbers = list(range(0,10))
def filterEven(l):
    
    n = []
    e = []
    for i in numbers:
        if(i%2==0):
            n.append(i)
        else:
            e.append(i)
    new = [n,e]
    return new


print(filterEven(numbers))
