#find avg of everyday, max sale 

sales = ([10,20],[12,22],[10,12],[34,56],[100,200],[90,76],[90,90])
avgList = []

for i,j in sales:
    avg = (i + j) // 2
    avgList.append(avg)

print(avgList) 

# for k in avgList:
#     if k > max:
#         max = k

maxvalue = max(avgList)

ind = avgList.index(maxvalue)

print(maxvalue)
print("index: ", ind + 1)

avgTuple = tuple(avgList)

maximum = max(avgTuple)
index = avgTuple.index(maximum)
print("Maximum value is: ", maximum)