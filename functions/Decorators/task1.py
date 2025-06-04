#check if all elements passed in args are numbers or not

def outer(fnc):

    def inner(*args):

        flag = True

        for i in args:
            if type(i).__name__ not in ['int', 'float']:
                flag = False
                break

        if flag:
            fnc(*args)
        # else:
        #     print("Other than numbers exist")

    return inner

# @outer
# def result():
#     print("All are numbers")

# result(1, 2, "1", True)

# task2 print squares of the numbers

@outer
def result(*args):
    for i in args:
        if type(i) != "int" or type(i) != "float": 
            print(i)
        else:
            print(i ** 2, "\t")

result(1, 2, True, "ABC")
