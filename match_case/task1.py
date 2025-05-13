print("Welcome!!!")

print("1. Single player\n2. Multi-player")

choice = int(input("Enter a number: "))

if choice == 1:
    print("You have selected single player mode.")
    toss = int(input("Enter 0 for batting and 1 for bowling: "))
    if toss == 0:
        print("You choose batting")
    else:
        print("You choose bowling")
elif choice == 2:
    print("You have selected multi-player mode.")

