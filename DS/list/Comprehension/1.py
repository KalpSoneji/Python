data = [1, -2, 3, 4, -5]

data2 = [i**3 for i in data if i % 2 == 0] 

data3 = [i**2 for i in range(1, 11)]

data4 = ["+ve" if i > 0 else "-ve" for i in data]

data5 = ["abc", "def", "", None, False]

data6 = [i for i in data5 if i] # "if i" checks each value, if its 0/None/False it doesn't accept

print(data6)