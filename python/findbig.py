num1  = int(input("enter the number : "))
num2 = int(input("enter the number2 : "))

def findbig(a,b):
    if a < b:
        return b
    else:
        return a
print(findbig(num1,num2))