#get start and end value from user, print numbers between them and their sum

sv = int(input("Enter starting value: "))
ev = int(input("Enter ending value: "))
sum = 0

for i in range(sv, ev+1):
    print(i, end=" ")
    sum += i

print("Sum of numbers between", sv, "and", ev, "is", sum)