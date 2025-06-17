with open("./File_Handling/tell_seek.txt",'r') as f:
    print("Current cursor position: ", f.tell())
    print(f.read(10))
    print("Current cursor position: ", f.tell())
    f.seek(0)
    print("Current cursor position: ", f.tell())
    print(f.read(10))
    print("Current cursor position: ", f.tell())
    print(f.read(10))
    print("Current cursor position: ", f.tell())

    #tell tells current cursor position
    #seek moves cursor position
