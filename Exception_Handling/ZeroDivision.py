try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    ans = a / b
    print(ans)

except ZeroDivisionError as e:
    print("Zero division error: ", e)

except ValueError as e:
    print("Value Error: ", e)

except Exception as e:
    print("EXCEPTION", e)

finally:
    print("The End!!!")

# finally gets run no matter what
# a particular hierarchy has to be followed while writing except blocks
# coz if we keep Exception at top, with any error it will be called