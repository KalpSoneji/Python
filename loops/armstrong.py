no = int(input("Enter a number: "))
count = 0
sum = 0

temp = no

while(temp != 0):
    rem = temp % 10
    count += 1
    temp //= 10

temp = no

while(temp != 0):
    rem = temp % 10
    sum = sum + (rem ** count)
    temp //= 10

if (no == sum):
    print(no,"is an Armstrong number")
else:
    print(no,"is not an Armstrong number")
