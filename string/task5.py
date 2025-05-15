#find index

name = input("Enter name: ")
find = input("Enter character: ")
flag = -1

for i in range(len(name)):
    if name[i] == find:
        flag = i
        break

print(find, " found at index ", flag)