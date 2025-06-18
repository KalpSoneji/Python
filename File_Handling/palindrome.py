list = ['naman','bob','raj','ram']

with open("./File_Handling/palindrome.txt", 'w') as f:
    for i in list:
        if i == i[::-1]:
            f.write(i + "\n")