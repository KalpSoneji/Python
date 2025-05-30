print("Enter names:")
string = input()

vowels = 'aeiouAEIOU'
names = string.split()
dict = {}

for name in names:
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    dict[name] = count

print(dict)