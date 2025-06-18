with open("./File_Handling/a.jpg", 'rb') as f:
    data = f.read()

with open("./File_Handling/binary1copy.jpg", 'wb') as f:
    f.write(data)

# works with any format except txt