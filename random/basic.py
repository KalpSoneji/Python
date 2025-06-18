import random

# x = random.random() # generates a float btw 0 and 1
# print(x)

# print(random.randint(1, 100)) # generates integer btw 1 and 100 (both included)

data = ["ram","shyam","amit","sumit"]
# name = random.choice(data) # chooses a random item from the list
# print(name)

# random.shuffle(data) # shuffles the list within itself
# print(data)

random.seed(7) # keeps printing a fix number
print(random.randint(1,100))