

# make a list in this we will convert the value in str


items = [1,2,3,4 , [1,2,3.5,4] , 4.5]
def new(a):
    return [str(i)  for i in items if type(i)==int or type(i)==float or type(i)==list]
print(new(items))
