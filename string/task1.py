#convert lower to upper without function

name = input("Enter a name: ")

for i in range(0, len(name)):
    # if(name[i].islower() == True):
    if(ord(i) >= 97 and ord(i) <= 122):
        print(chr(ord(name[i]) - 32), end = "")
    else:
        print(name[i], end = "")  
