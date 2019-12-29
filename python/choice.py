import random 

value = random.randint(1,100)
win = int(input("enter the any number beetween 1 to 100 : "))
count = 0

while(True):
    if value==win:
        print(f"hey you have win!!!!!!!!!!!!!!  in  {count} times")
        break
    elif value < win:
        print ("value is greater !!!!!!!!!!!")
        count+=1
    elif value > win:
        print("value is low!!!!!!!!")
        count+=1     
    else:
        print("please enter a valid input")
        count+=1
    win = int(input(" try again beetween 1 to 100 : "))
    continue