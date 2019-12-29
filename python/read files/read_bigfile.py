# with open('home.html' , 'r') as f:
#     print(f.read(100))
#     print(f.read(100))


# you can use while loop with your file

with open('home.html' , 'r') as f:
    data = f.read(100)
    while len(data) > 0:
        print(data)
        data  = f.read(100)
    