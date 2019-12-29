
numbers = list(range(1,5)) # 4,3

                             
def reverse(l):
    rev = [] # 4 ,3
    for i in range(len(l)):
       rev.append(l.pop())
    return rev

print(reverse(numbers))
        
numbers = list(range(1,5)) # 4,3
def reverse2(l):
    l.reverse()
    return l
print(reverse2(numbers))

numbers = list(range(1,5)) # 4,3
def reverse3(l):
    return l[::-1]
    
print(reverse3(numbers))