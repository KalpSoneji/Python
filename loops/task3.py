# take a number and print its factorial

no = int(input("Enter a number: "))
fact = 1

for i in range(no, 0, -1):
    fact *= i

print(fact)