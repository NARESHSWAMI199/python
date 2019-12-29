

# this method will give error that you don't pass any agruments then don't get i for i**a then this will show error


# nums = input("enter the some numbers using comma : " ).split(",")

# def nums_opreations(a,*args):
#     return [ int(i)**a if args else "please pass some arguments" for i in args ]


#----------------------------------------------------------------------------------------------------
# error beacuse the else condition not come in for loop beacuse if args not pass the vlaue is 0 and the 0 then for loop not run
# when for loop go to zero then  else condition not print and if one args given the work
#-------------------------------------------------------------------------------------------------------

# print(nums_opreations(3,*nums))



# right way this

# nums = input("enter the some numbers using comma : " ).split(",")

# def nums_opreations(a,*args):
#     if args:
#         return [ int(i)**a for i in args ]
#     else :
#         print ("please enter some vlaue")


# print(nums_opreations(3,*nums))