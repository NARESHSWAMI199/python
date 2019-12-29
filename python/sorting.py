

# normal we have asign a fuction like this
numbers = [1,3,2,5,1]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i] , numbers[j] = numbers[j],numbers[i] 
print(numbers)



tuple_len = int(raw_input())
a = tuple(map(int, raw_input().split(' ')))
print hash(a)