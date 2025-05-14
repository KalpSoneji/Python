a = 0
b = 1
print(a, b, end = " ")

for i in range(1, 10):
    sum = a + b
    print(sum, end = " ")
    a = b
    b = sum
