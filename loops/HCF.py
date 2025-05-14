no1 = int(input("Enter a number: "))
no2 = int(input("Enter another number: "))
temp = 0

while no2 != 0:
    temp = no2
    no2 = no1 % no2
    no1 = temp

print("HCF = ", no1)