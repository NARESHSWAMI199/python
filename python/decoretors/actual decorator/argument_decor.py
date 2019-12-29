from functools import wraps

def all_are_type(data_type):
    def decorator(fun):
        @wraps(fun)
        def wrapper(*args,**kwargs):
            if all([type(i)==data_type for i in args]):
                return fun(*args,**kwargs)
            else:
                print("invalid args")
        return wrapper
    return decorator


@all_are_type(str)
def display(*args,**kwargs):
    return (f"the value is the {args}")

print(display("naresh","swami",[3,4]))
