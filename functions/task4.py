#pass all arguments in args, just print the sum of numbers(int, float)

def ans(*args):
    # return sum(i for i in args if type(i).__name__ == 'int' or type(i).__name__ == 'float')
    sum = 0
    for i in args:
        if type(i).__name__ == 'int' or type(i).__name__ == 'float':
            sum += i
    return sum


print(ans(100, True, 20, 20.89, 100, "java", 90.90, "C", False, "Python"))