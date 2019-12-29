# gentrator are itarators mean simple we can use on this direct next() function noy iter() func


def square():
    for i in range(1,5):
        i**2
        yield i
nums =  square()

for i in nums:
    print(i)


# for i in nums:
#     print(i)     you can use the for loop only one time beacuse gentator create the value on dimand and remove previous 
# values