users = ['ram',"shyam","amit","sumit","ajay","jaya"]

with open("./File_Handling/users.txt","a") as file:
    file.writelines(i + '\n' for i in users)