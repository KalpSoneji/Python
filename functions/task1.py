def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

def calculator():   
    ans = []

    while True:
        print("\n--- Calculator Menu ---")
        print("Enter 1 for add")
        print("Enter 2 for sub")
        print("Enter 3 for mul")
        print("Enter 4 for div")
        print("Enter 5 to get all answers")
        print("Enter 6 to exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1 | 2 | 3 | 4:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == 1:
                    result = add(a, b)
                    operation = f"Addition: {a} + {b} = {result}"
                elif choice == 2:
                    result = sub(a, b)
                    operation = f"Subtraction: {a} - {b} = {result}"
                elif choice == 3:
                    result = mul(a, b)
                    operation = f"Multiplication: {a} * {b} = {result}"
                elif choice == 4:
                    result = div(a, b)
                    operation = f"Division: {a} / {b} = {result}"

                print("Result:", result)
                ans.append(operation)

            case 5:
                if not ans:
                    print("No operations performed yet.")
                else:
                    print("\n--- All Performed Operations ---")
                    for item in ans:
                        print(item)

            case 6:
                print("Exiting calculator.")
                break

            case _:
                print("Invalid choice! Please try again.")
                break

calculator()