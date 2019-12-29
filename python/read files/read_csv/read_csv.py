from csv import reader

with open('file.csv','r') as f:
    p = reader(f)
    next(p)
    for i in list(p):
        print(i)
    