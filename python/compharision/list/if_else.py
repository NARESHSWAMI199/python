
# make a find even numbers programe 


# numbers = list(range(1,11))
# # find even
# new = []
# for i in numbers:
#     if i%2==0:
#         new.append(i)
# print(new)

# numbers = list(range(1,11))
# even = [i for i in numbers if i%2==0 ]
# print(even)


# # print odd 

# odd = [i for i in range(1,11) if i%2 != 0]
# print(odd)




# MUST REMEMBER IN THAT WHEN YOU USE ONLY IF STATMENT THE WRITE IN LAST AND WHEN YOU USE ELSE CONDITION OR ELIF CONDITION 
# THEN WRITE IN FIRST
# LIKE THIS

# what we doing if the number is even then his square and odd then nagative

new = [i**2  if i%2==0  else -i  for i in range(1,11)]
print(new)