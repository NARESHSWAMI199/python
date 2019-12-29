
# the zip function is itertor this will direct call next function for display content


users = ["user1 " ,"user2" , "user3"]
names = ["naresh" , "manish" ]

# ('user1 ', 'naresh') ('user2', 'manish')

# if you remove one name or user from list then this will return like

# for join to these list in a manged way use zip function this will return pair of tuples


# like  ("user1", "naresh") , ("user2" "manish") , ("user3" , "mintu")
# you can directly change in dict or list , tuples...


new = dict(zip(users,names))
print (new)


# you can use for loop for print a itertor

# new1 = zip(users,names)

# for i in new1:
#     print (i)



# change Zip output again in list like

new = [ (1,2),(3,4),(5,6),(7,8)]
n,n2 = zip(*new)

print (list(n),list(n2))



# l1 = [1,2,3,4]
# l2 = [5,6,7,8]

