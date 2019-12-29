# access the value form a dict

names = {
  'presion1' : {'name' : 'naresh','age' :24},
    'presion2' : {'name' : 'nsh','age' :14},
}

# you can't store a list or tuple or dict in a dict whitout his key

print ([names[name]['name'] for name in names])


# find the max score using max() function

students  = {
    'naresh ' : {'score' : 45 ,'age':20 },
    'manish ' : {'score' : 65 ,'age':23 },
    'chanda ' : {'score' : 85 ,'age':20 },
}

# you can access the value like this
print([students[items]['age'] for items in students])

print(max(students , key= lambda items: students[items]["score"]))


