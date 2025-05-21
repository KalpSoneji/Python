#number key value pair
#make a new dict where value is even

dict = {1 : 100, 2 : 123, 3 : 456, 4 : 789, 5 : 200}
dict1 = {}

for i, j in dict.items():
    if j % 2 == 0:
        dict1[i] = j
        
print(dict1)

