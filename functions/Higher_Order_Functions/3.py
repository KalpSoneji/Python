def sci(name):
    print(f"{name} has took admission in science")

def com(name):
    print(f"{name} has took admission in commerce")

def arts(name):
    print(f"{name} has took admission in arts")

def main(cb, name):
    print("Taking admission")
    cb(name)

name = input("Enter your name: ")

perc = float(input("Enter your %: "))

if perc > 90:
    main(sci, name)

elif perc > 80:
    main(com, name)

else:
    main(arts, name)