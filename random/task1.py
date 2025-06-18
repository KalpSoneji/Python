import random

name = input("Enter your name: ")

count = 0

for i in range(6):
    x = random.randint(1, 6)
    if x == 6:
        count += 1
    print(x)

print("Count = ", count)