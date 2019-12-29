

# finding highest length of the item in list using max () function

nums = [1,2,3,4,5656,4,567]
print(max(nums))

# simple the max function first unpack the list and the compare 

names = ['naresh swami', 'abcdefchijklmnopqurest' , 'abc','manish']
# print(max(names))   this will not give a right answer
print(max(names , key= lambda item : len(item)))

# simple here passed the lists values

 

# the key value use for the which bases you want search



# find the max score using max() function

students  = {
    'naresh ' : {'score' : 45 ,'age':20 },
    'manish ' : {'score' : 65 ,'age':23 },
    'chanda ' : {'score' : 85 ,'age':20 },
}


print(max(students , key= lambda items: students[items]["score"]))