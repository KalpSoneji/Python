no1 = int(input("Enter 1st number: "))
no2 = int(input("Enter 2nd number: "))

if no1 > no2:
    max = no1
else:
    max = no2

lcm = 0

while True:
    if((max % no1 == 0) and (max % no2 == 0)):
        lcm = max
        break
    max += 1

print("LCM = ", lcm)