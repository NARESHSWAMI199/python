name = input("enter the your name : ")
age = input("enter the your age : ")
fav_movies= input("enter the your fav movies : ").split( ",")
fav_songs = input("enter the you fav songs : ").split(",")   # this will give a list also 



new = {}
new["name"] = name
new["age"] = age
new["fav_movies"] = fav_movies
new["fav_songs"] = fav_songs


for i, j in new.items():
    print(f" {i}  : {j}")