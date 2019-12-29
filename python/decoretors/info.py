
def square(a):
    return a**2


# you can write like this also beacuse here the s hold also the square function
s = square
print(s(7))

print(s.__name__)
print(square.__name__)

print(s)
print(square)