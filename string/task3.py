#count whitespaces

count = 0
name = input("Enter a name: ")

for i in name:
    if(' ' in i):
        count += 1

print("Total whitespaces: ", count)