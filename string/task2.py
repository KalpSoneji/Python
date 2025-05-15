#check for palindrome

name = input("Enter a name: ")
rev = ''

for i in range(len(name) - 1, -1, -1):
    rev += name[i]
    
print("Reverse of what you entered is: ", rev)

if name == rev:
    print("Palindrome")
else:
    print("Not palindrome")  