numbers = list(range(1,5))
number2 = [1,3,5,7,8]

def check_Equal(l,l2):
    new = []
    for i in l:
        if i in l2:
            new.append(i)
    return new
        
print(check_Equal(number2,numbers))