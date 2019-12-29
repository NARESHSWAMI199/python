
def sum_mul(a,b):
    add = a+b
    mul = a*b
    return add, mul

print(sum_mul(1,2))  # give tuple

m,n = sum_mul(1,2)  # unpacking tuple
print(f"{m} , {n}")