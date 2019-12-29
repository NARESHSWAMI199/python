

def outerfunc(msg):
    def inner():
        print(f"the message is the {msg}")
# here i will not calling function only return 
    return  inner
    
var = outerfunc("hello am nsfuntu s")

var()

# actullay what happen here that the fuction will return a function and that function hold the var 
# and when we call the var the this will react like a function beacuse this is also  inner function which
# returned by the outer func

