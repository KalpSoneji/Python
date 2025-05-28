def fnc(a=1, b=2):
    return a + b

print(fnc(4, 5))
print(fnc()) #when no argument is passed, it will use the default values
print(fnc(3)) #when one argument is passed, it will use the default value for the other
print(fnc(b=10)) #when one argument is passed with keyword, it will use the default value for the other
print(fnc(a=5, b=6)) #when both arguments are passed with keyword, it will use the passed values
print(fnc(a=5)) #when one argument is passed with keyword, it will use the default value for the other
