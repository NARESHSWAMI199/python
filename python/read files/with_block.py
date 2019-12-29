

with open('hello.html') as f:
    data  = f.read()
    print (data)
print (f.closed)  # the will auto closed
    