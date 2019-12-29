from csv import DictWriter

with open('file2.csv','a',newline='') as f:
    data = DictWriter(f,fieldnames=['name','lastname','age'])
    data.writeheader()  # this wite the fieldname in our file
           
    data.writerow({
        'name' : 'naresh',
        'lastname': 'swami',
        'age' : 20
    })
    data.writerow({
        'name' : 'manish',
        'lastname': 'swami',
        'age' : 23
    })


    data.writerows([{'name' : 'manish','lastname': 'swami','age' : 23},
    {'name' : 'manish','lastname': 'swami','age' : 23 }
    ])