age = int(input("Enter age: "))

try:
    if age<18:
        raise ValueError("Above 18 only")
    else:
        print("Eligible")

except ValueError as e:
    print("Error: ", e)