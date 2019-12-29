
name = ["abc","tuv","cda"]

def reverse(a):
    new = [i[::-1] for i in a ]
    return new
print(reverse(name))


# # you can use also like this

# def reverse(a):
#     return [i[::-1] for i in a ]
# print(reverse(name))