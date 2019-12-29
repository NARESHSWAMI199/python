fruits1 = ['mango','apple']
fruits2 = ['chili','ok']

fruits = fruits1+ fruits2
print(fruits) #     ['mango', 'apple', 'chili', 'ok']

#----------------

fruits1.extend(fruits2)
print(fruits1)  #   ['mango', 'apple', 'chili', 'ok']

#--------------------


fruits1.insert(1 ,'grapes')
print(fruits1)  #   ['mango', 'grapes', 'apple', 'chili', 'ok']

#-----------------------

fruits1.append(fruits2)
print(fruits1)  #   ['mango', 'grapes', 'apple', 'chili', 'ok', ['chili', 'ok']]