#remove duplicates

data = ['ram', 'shyam', 'seeta', 'shyam', 'ajay', 'ram']
unique = []

for i in data:
    if i not in unique:
        unique.append(i)

print(unique)