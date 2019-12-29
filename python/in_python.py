name = "naresh"
world = input("enter the name : ")
if world in name:
    print(f"yes this is present on index {name.find(world)}")
else:
    print("yes this is not present ")