
# if you use like this then this is a set

# even_odd= {f"even {i}" if i%2==0 else f"odd {i}" for i in range(1,11)}
# print(even_odd)
# print(type(even_odd))


# how make dict

even_odd1 = { i:('even' if i%2==0 else "odd" ) for i in range(1,11)}
print(even_odd1) 
print(type(even_odd1))