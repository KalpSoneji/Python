# data = [1, 2, 3, 4, 5]

# list = list(filter(lambda x : x % 2 == 0, data))

# print(list)

name = ["amit","sumit","jay","",None,"raj","parth",None,"kunal","smit","sanjay"]

x1 = filter(lambda x: x and len(x)>4, name)
print(list(x1))

x2 = filter(lambda x: x and x.startswith('s'),name)
print(list(x2))

x3 = filter(lambda x: x,name)
print(list(x3))

#write such conditions that return in True or False
#we can use 1. and 2. or 3. not

#lambda x makes sure its not None or isn't an empty string, hence we used and with it so error doesn't appear