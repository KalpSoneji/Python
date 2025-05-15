name = input("Enter a name: ")

for i in range(len(name)):
    if name[i] == ' ':
        print('', end = '')
    else:
        print(name[i], end='')

