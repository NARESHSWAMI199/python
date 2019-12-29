import time

t = time.time()
list1 = [i**2 for i in range(100000)]
t1 = time.time()
print(t1-t)
t2 = time.time()
list = [i**2 for i in range(100000)]
t3 = time.time()
print(t3-t2)
