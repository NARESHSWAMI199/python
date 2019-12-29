name = input("enter the your name : ")
temp = ""

for i in name:
    if i not in temp:
        print(f"{i} is coming time {name.count(i)}")
        temp+=i
        


