# Higher-Order Function: Adds extra behavior to the target function

def order_food(func):

    def wrapper():

        print("Ordering food...")  # Pre-processing step
        func()                     # Original function call
        print("Food has been delivered!")  # Optional post-processing

    return wrapper

# Decorator applied to the function
@order_food
def throw_party():
    print("Throwing a party!")

# Function call (triggers decorated version)
throw_party()