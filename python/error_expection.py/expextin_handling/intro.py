

try:
    age = int(input("enter the your age : ")) # seven
except :
    print ("unknow error")
else:
    if age < 18:
        print ("sorry you can't watch movie")
    else : 
        print ("you can watch movie")
finally :
    print ("this is finally block this is always run")
