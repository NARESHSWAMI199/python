

def sum(*args):
    add =0
    if all([type(arg) == int or type(arg)==float for arg in args]):
        for i in args:
            add+=i
    else :
        return "worng input"
    return add
    
print(sum([1,3,4,5]))
    
                