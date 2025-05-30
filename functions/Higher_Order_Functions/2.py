def sci():
    print("Science")

def com():
    print("Commerce")

def arts():
    print("Arts")

def main(cb):
    print("Admission done...")
    cb()

perc = float(input("Enter your %: "))

if perc > 80:
    main(sci)

elif perc > 70:
    main(com)

else:
    main(arts)