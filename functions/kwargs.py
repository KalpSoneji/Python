# def fnc(**kwargs):
#     print(kwargs)

# fnc(name="ram", age=23, email="ram@gmail.com", status=True)  # works with any number of keyword arguments, dictionary only

def fnc(x, **kwargs):
    print(x, kwargs)

fnc(x=10, name="ram", age=23, email="ram@gmail.com", status=True)

