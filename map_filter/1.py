name = ["amit","sumit","jay","",None,"raj","parth",None,"kunal","smit","sanjay"]

new = filter(lambda x : x and x.startswith('S'), map(lambda x : x and x.title(), name))

print(list(new))