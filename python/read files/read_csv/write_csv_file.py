from csv import writer

with open('file2.csv','a',newline='') as wf:
    data = writer(wf)
    # # there are two method that are the writerow and wirterows
    # data.writerow(['name','country'])
    # data.writerow(['naresh','India'])
    # data.writerow(['manish','India'])
       
    data.writerows([['name','country'],['naresh','India'],['manish','India']])