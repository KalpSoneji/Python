# with open("./File_Handling/data.txt",'r') as f:
#     data = f.read()
#     print(data)

# with open("./File_Handling/data.txt",'r') as f:
#     data = f.readline() #can take size in arg
#     print(data)


# with open("./File_Handling/first.txt",'r') as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         print(line.strip())

with open("./File_Handling/first.txt",'r') as f:
    for data in f:
        print(data.strip())

# with open("./File_Handling/data.txt",'r') as f:
#     lines = f.readlines()
#     print(lines)