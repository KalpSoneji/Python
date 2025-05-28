#print max from args

# def fnc(*args):
#     print(max(args))

# fnc(10, 10, 100, 9, 70, 65, 0)

#create a fnc which takes 2 arguments, first threshold and second *args, return [100, 70, 65] using comprehension

# def ans(x, *args):
#     return [i for i in args if i > x]

# print(ans(10, 10, 100, 9, 70, 65, 0))

#if we want to keep x at last, at the time of calling, we can use keyword argument

def ans(*args, x):
    return [i for i in args if i > x]

print(ans(10, 10, 100, 9, 70, 65, 0, x=10))