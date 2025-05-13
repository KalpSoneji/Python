age = int(input("Enter age: "))

if age >= 18:
    if age >= 21:
        print("You can both marry and drive.")
    else:
        print("You can drive but not marry.")
else:
    if age >= 16:
        print("You can drive an EV vehicle.")
    else:
        print("Take an uber.")