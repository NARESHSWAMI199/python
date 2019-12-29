
n = int(input())
nums = lambda n : (i for i in range(1,n+1) if i%2==0)
nums=nums(n)
for i in nums:
    print (i ,end=" ")
    
