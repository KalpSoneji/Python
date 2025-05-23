data = {"op_sindoor" : ["PM", "HM", "DM", "Army", "Navy"], "URI" : ["PM", "HM", "DM", "Army"]}

# print(data["op_sindoor"])

op_sindoor = data["op_sindoor"]

# for i in op_sindoor:
#     print(i)

for i, j in data.items():
    print(i, end = " ")

    for k in j:
        print(k, end = " ")
        
    print()