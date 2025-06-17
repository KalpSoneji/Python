with open("./File_Handling/data.txt","r") as file:
    header_p = False 
    while True:
        position = file.tell() 
        print(position)
        line = file.readline()
        
        if not line:
            break
        
        if line.startswith("Header"):
            if not header_p:
                print("Keeping Header",line.strip())
                header_p = True
            else:
                print("skiiping header")
                file.seek(file.tell())    
        else:
            print(line.strip())                                                                                                                                     