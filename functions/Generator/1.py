# def my_fun():
#     return 1
#     return 2


# x = my_fun()
# print(x)

# over here, we can't return multiple values as flow gets transferred
#hence, we use yield

def my_fun():
    yield 1 
    yield 2 
    yield 3
    yield 4
    yield 5

gen = my_fun()
for i in gen:
    print(i)