numbers = [1,2,3 ,[4,5,6],4,5,[5,6],[4,6]]

def lists_in_list(l):
    total = 0
    for i in numbers:
        if type(i) == list:
            total+=l.count(i)
    return total

print (lists_in_list(numbers))