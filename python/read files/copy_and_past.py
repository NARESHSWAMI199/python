with open('file.txt','r') as rf: 
    with open('naresh.txt','w') as wf:
        wf.write(rf.read())