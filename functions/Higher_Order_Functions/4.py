def goa(name):
    print("Goa")
    return "Kaju"

def abu(name):
    print("Abu")
    return "Rabdi"

def park(name):
    print("Parimal")
    return "Corn"

def main(cb):
    print("Main")
    x = cb("Kalp")
    print("Food = ", x)


budget = float(input("Enter budget: "))

if budget > 10000:
    main(goa)

elif budget > 5000:
    main(abu)

else:
    main(park)
