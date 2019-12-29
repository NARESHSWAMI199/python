from csv import DictReader, DictWriter

with open('file2.csv','r') as rf:
    with open('file3.csv','a',newline='') as wf:
        r_data = DictReader(rf)
        w_data = DictWriter(wf,fieldnames=['name','last','age'])
        w_data.writeheader()

        for row in r_data:
            name,last,age = row['name'],row['lastname'],row['age']
            w_data.writerows([
                {
                    'name' : name,
                    'last' : last,
                    'age'  : 20
                }
            ])