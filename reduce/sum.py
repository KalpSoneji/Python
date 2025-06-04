from functools import reduce

num = [i for i in range(1, 11)]

sum = reduce(lambda x, y : x + y, num)

print(sum)