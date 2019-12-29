


# def multiply(*args):
#     mul = 1
#     print(f" args is {args}")
#     for i in args:
#         mul *= i 
#     return mul

# nums  = [2,3,4]  # if we pass only a list then *args take only one argument then how to unpack the list element 

# print(multiply(nums))  

# this output is 
#   args is ([2, 3, 4],)
#   [2, 3, 4] 


# beacuse =  1*[2,3,4]




def multiply(*args):
    mul = 1
    print(f" args is {args}")
    for i in args:
        mul *= i 
    return mul

nums  = [2,3,4]
print(multiply(*nums))   # use star opreator for unpack list or tuple


# this output is


# args is (2, 3, 4)
# 24