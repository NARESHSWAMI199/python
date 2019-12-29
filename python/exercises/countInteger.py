

# count an integer array
a = " "
array = [1,2,3,52,3,4,2]


for i in array:
    count = array.count(i)
    if str(i) not in a:
        a+=str(i)
        print( int(i) ," : ",count)
     
        
    