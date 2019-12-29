


# Now we learn that how to actual syntax of the decorator

# i want print one more line with our function this is like

# this is a awsome function


def decorator(func):
    def wapper():
        print("this is a awsome function ")
        func()
    return wapper


# @ use of this 

# actually when you use @ with your function then the first called your function  and pass your secound function as
# an argument 

@decorator
def func1():
    print ("this is function one")
@decorator
def func2():
    print("this is function2")

func1() # here can directly call the dectorater function is this shortcut
func2()

# func1 = decorator(func1)
# func1()