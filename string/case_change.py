text = input("Enter a string: ")

for char in text:
    if char >= 65 and char <= 90:
        ord(char) += 32
    elif char >= 97 and char <= 122:
        ord(char) -= 32

print(text)