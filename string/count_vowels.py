vowels=0
consonants=0

a = input("Enter a string: ")

for char in a:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1
    
    elif char == ' ':
        continue
    
    else:
        consonants += 1

print("Vowels = ", vowels)
print("Consonants = ", consonants)

