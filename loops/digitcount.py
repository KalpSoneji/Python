no = int(input("Enter a number: "))
count = 0

while no != 0:
    no //= 10
    count += 1

print(count)