#print all day data:
#remove netflix from monday
#remove yt from all day history

history = [["yt","netflix","inst","yt","yt","prime"],["hotstar","yt","prime","netflix"],
           ["yt","netflix","gpt","yt","yt","gpt"],["hotstar","yt","prime","google"]]

# print(history)

y = history[0]
j = 0
while j < len(y):
    if y[j] == "netflix":
        y.pop(j)
    else:
        j += 1

print(history)

for x in history:
    #x = ["yt","netflix","inst","yt","yt","prime"]
    i =0 #i=0
    while i<len(x): #3<6 True
        if x[i] == "yt": #x[0] == "netflix"
            x.pop(i) # yt pop
        else:
            i+=1

print(history)                    
