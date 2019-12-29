x = 5 

def display():
    global x  # you mention that you are working with gobal var
    x = 7
    return x

print(display())
print(x)