def fibo_series(n):
    a = 0
    b= 1

    if n==1:
        print(a)
    elif n==2:
        print (a,b)
    else :
        print(a , b , end = ",")
        for i in range(n-2):
            c = a + b  # a =0 and b =1 | a = 1 , b = 1 | a = 1 , b = 2 | a = 2 , b = 3
            a = b # a =1 | a = 1 | a = 2 | a = 2
            b = c   # b = 1 | b = 2 | b = 3 | b = 5   <<<-----see here <<------
            print(b , end= ",")

    
   
fibo_series(10)