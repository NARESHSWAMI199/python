

# this method take args as a dict and pass a dict


def display(**kwargs):
    for i , j in kwargs.items():
        print(f"{i} : {j}")

# display(1,2,3)  # don't take arguments like this

# display(name ="naresh" , last_name = "swami")

d = {"name": 'naresh' ,"surname":"swami"}
# display(d)  # this will give error beacuse the  kwargs takes only unpaked dict

# slove

display(**d)  # this will upack
  


# if you pass a one more perameter then you must pass this as a arguments

# and for unpaking dict use the **dict