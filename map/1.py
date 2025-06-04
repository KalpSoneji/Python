data = [1, 2, 3, 4, 5]

set = set(map(lambda x : x**2, data))
list = list(map(lambda x : x**2, data))
tuple = tuple(map(lambda x : x**2, data))

print(set)
print(list)
print(tuple)

#first arg: function, gotta be lambda coz its single line
#2nd arg: any iterable object = list, dict