with open("file.txt") as f:
    with open('file2.txt' ,'a') as wf:
        for i in f.readlines():
            name,salary = i.split(',')
            wf.write(f"{name}'s salary is {salary}")