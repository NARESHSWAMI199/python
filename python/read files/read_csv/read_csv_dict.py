from csv import DictReader

with open("file.csv") as f:
    data = DictReader(f, delimiter=',')
    for i in data:
        print (i['name'])

 