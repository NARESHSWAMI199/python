names = ["abc","tuv","xyz"]

def reverse(l):
    new= []
    for i in names:
        new.append(i[::-1])
    return new


print(reverse(names))