list = [1,2,3,4,5,6]
list1=[]

for i in list:
    if i % 2 == 0:
        list1.append(i)

print("Even number list: ", list1)
print("No. of even numbers: ", len(list1))