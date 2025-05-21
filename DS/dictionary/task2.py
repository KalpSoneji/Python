#string dictionary
#if starts with s / len > 5 / palindrome add to new dict

data = {"a" : "Kalp"}
new_dict = {}
data.update({"b" : "Vatsal", "c": "Harshita", "d" : "sujal", "e" : "madam"})

pairs = data.items()

print(pairs)

for i, j in pairs:
    if j[0] == 's' or len(j) > 5 or j == j[::-1]:
        new_dict[i] = j

print(new_dict)  
