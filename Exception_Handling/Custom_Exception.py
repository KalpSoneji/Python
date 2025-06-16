class InvalidAgeException(Exception):
    def __init__(self, message): #param message
        super().__init__(message) #

name = input("Enter name: ")        

try:
    if " " in name:
        raise InvalidAgeException("Space found")
    else:
        print(f"{name}")

except InvalidAgeException as e:
    print(f"{e}")        