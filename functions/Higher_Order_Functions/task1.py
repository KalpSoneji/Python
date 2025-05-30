def bat(name, runs):
    print(f"{name} scored {runs} runs!")

def bowl(name, wickets):
    print(f"{name} took {wickets} wickets!")

def wk(name, lname): 
    print(f"{name} took the catch of {lname}!")

def main(cb, *args):
    fname = input("Enter your name: ")
    return cb(fname, args)

role = input("Enter your role: ")

if role == 'bat':
    runs = float(input("Enter runs: "))
    main(bat, runs)

elif role == 'bowl':
    wickets = float(input("Enter wickets: "))
    main(bowl)

else:
    lname = input("Enter the name of the batsman dismissed: ")
    main(wk, lname)
