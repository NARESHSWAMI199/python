
class NameShortError(NameError):
    pass

def length(name):
        if len(name) < 8 :
            raise NameShortError("sorry name is very short")
        else:
            print(f"hello {name} your welcome")

name = input()
length(name)