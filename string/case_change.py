text = input("Enter a string: ")

for char in text:
    if ord(char) >= 97 and ord(char) <= 122:
        print(chr(ord(char)-32), end="")
    elif char == ' ':
        print(" ", end="")
    else:
        print(chr(ord(char)+32), end="")
        
# print(text)