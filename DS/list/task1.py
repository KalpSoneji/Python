#sort list acc to odd and even

data = [1, 2, 3, 4, 5]
even = []
odd = []

for i in range(len(data)):
    if data[i] % 2 == 0:
        even.append(data[i])
    else:
        odd.append(data[i])

print("Odd: ", odd)
print("Even: ", even)