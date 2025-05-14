no = int(input("Enter a number: "))
sum = 0

while no > 0:
    rem = no % 10
    sum += rem
    no = no // 10

print(sum)