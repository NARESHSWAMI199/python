name = input("enter the name for check is palindrom : ")

def is_plaindrom (a):
    if a[::-1] == a:
        print("this is a plaindrom string ")
    else :
        print("this is not an plain drom string")

is_plaindrom(name)

def is_plaindrom2(a):
    return a ==a[::-1]
print(is_plaindrom2(name))