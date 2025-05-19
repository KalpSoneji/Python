text = input("Enter a string: ")

rev = ""
word = ""

for char in text:
    if char == " ":
        rev += word[::-1] + " "
        word = ""
    else:
        word += char

rev += word[::-1]

print(rev)
