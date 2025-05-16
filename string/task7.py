#hi this is malayalam in india
#find longest word

# data = "hi this is malayalam in india"

# words = data.split(" ")
# longest_word = ""

# for i in range(len(words)):
#     if len(words[i]) > len(longest_word):
#         longest_word = words[i]
        
# print(longest_word)  

data = "hi this is malayalam in india #india #malayalam1"
current_word =""
longest_word = ""
current_len =0
longest_len =0

for ch in data + " ": 
    if ch!= " ": 
        current_word+=ch  
        current_len+=1   
    else:
        if(current_len>longest_len): 
            longest_len = current_len 
            longest_word = current_word
            
        current_word=""    
        current_len=0     

print("longest word = ",longest_word)        
print(data)