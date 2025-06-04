from functools import reduce

num = [12, 34, 56 ,78 ,90]

max = reduce(lambda x, y : x if x > y else y, num)

print(max)