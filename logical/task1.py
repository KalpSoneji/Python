sub1 = int(input("Enter marks: "))
sub2 = int(input("Enter marks: "))
sub3 = int(input("Enter marks: "))
sub4 = int(input("Enter marks: "))
sub5 = int(input("Enter marks: "))

perc = (sub1 + sub2 + sub3 + sub4 + sub5) // 5

if perc >= 80:
    print("Grade: A")
elif perc >= 70:
    print("Grade: B")
elif perc >= 60:
    print("Grade: C")
elif perc >= 35:
    print("Grade: D")
else:
    print("Failed")
