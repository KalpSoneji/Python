#make duplicate elements list

data = ['ram', 'shyam', 'seeta', 'shyam', 'ajay', 'ram']
data2 = []
data3 = []

for i in data:
    if i not in data2:
        data2.append(i)
    else:
        data3.append(i)

print(data3)
