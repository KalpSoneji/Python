# create udf function accept *args as param and sum of all numners
# if args has anny other datatype except int raise TypeError with message "Only numbers are allowed"


def fnc(*args):
    sum = 0

    try:
        # list = input("Enter numbers: ")
        for i in args:
            if type(i).__name__ == 'int':
                sum += i 

            else:
                raise TypeError("Non-Integer found (RAISE)")

    except TypeError as e:
        print("Non-Integer found (EXCEPT)", e)

    finally:
        print(sum)

fnc(1, 2, 3, "a")