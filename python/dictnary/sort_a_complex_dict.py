

# we sort this according to the score  using sorted() method we can use this tuple also 
# for tuple the sort() method dont work but this will work and return a list 
students  = [
    {'score' : 45 ,'age':20,"name" :'naresh' },
    {'score' : 5 ,'age':23 , "name" :'manish'},
    {'score' : 85 ,'age':20 , "name" : 'rakesh'}
]

print(sorted(students, key = lambda item : item['score']))

# we can also reverse this like this
print(sorted(students, key = lambda item : item['score'] ,reverse = True))


