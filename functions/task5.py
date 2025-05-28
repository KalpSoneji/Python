def fnc(op, *args):
    total = 0
    product = 1

    for i in args:
        if type(i).__name__ == 'int' or type(i).__name__ == 'float':
                total += i
                product *= i

    if op == 'sum':
        return total
    elif op == 'mul':
        return product

print("Sum = ", fnc('sum', 100, True, 20, 20.89, 100, "java", 90.90, "C", False, "Python"))  
print("Product = ", fnc('mul', 100, True, 20, 20.89, 100, "java", 90.90, "C", False, "Python"))