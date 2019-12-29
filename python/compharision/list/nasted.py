

name = [["naresh","swami"] , [1,2,3,4,5],["rakesh",1,"manish"]]

# unpake in a list or tuple

new = [j    for i in name for j in i]
print(type(new))
print(new)

# numbers = [1,2,3,3,32,5,6,34]
# new1 = [numbers[i] (numbers[i],numbers[j] = numbers[j],numbers[i]) for i in numbers for j in range(i+1,len(numbers))   if numbers[i] < numbers[j] ]