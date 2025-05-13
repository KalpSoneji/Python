num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

choice = int(input("Enter operation: "))

match choice:
    case 1:
        print("Sum = " + str(num1 + num2))
    case 2:
        print("Difference = " + str(num1 - num2))
    case 3:
        print("Product = " + str(num1 * num2))
    case 4:
        print("Quotient = " + str(num1 / num2))
    case _:
        print("Invalid choice")
