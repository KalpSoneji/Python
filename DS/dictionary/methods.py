data = {"Gujarat" : "Gandhinagar", "Punjab" : "Chandigarh"}

k = data.keys()
print("Keys: ", k)

v = data.values()
print("Values: ", v)

data["Haryana"] = "Chandigarh"

data.update({"TN" : "Chennai", "Kerala" : "Thiruvananthapuram"})

kv = data.items()
print("Key-Value Pairs: ", kv)

data.pop("Punjab")

data.popitem()

for i, j in data.items():
    print(i, j)