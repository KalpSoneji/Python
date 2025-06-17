#product name: pen
#product price: 100
#------------------

with open("./File_Handling/task2.txt",'a') as f:
    while True:
        name = input("Enter product name: ")

        if name == 'exit':
            break

        price = input("Enter price: ")

        f.write(f"Product Name:  {name}\nProduct Price: {price}\n----------------------\n")