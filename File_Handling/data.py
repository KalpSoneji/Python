with open("./File_Handling/data.txt",'a') as f:
    while True:
        name = input("Enter your name: ")
        
        if name == 'exit':
            break

        no1 = int(input("Enter a number: "))
        no2 = int(input("Enter a number: "))

        sum = no1 + no2

        f.write(f"{name} : {sum}\n")

