
# nasted list 

# we will make a list like [[1,2,3] ,[1,2,3],[1,2,3] ]

new = [ [i for i in range(1,4)]  for j in range(3) ]
print(new)