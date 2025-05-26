#create new set of palindrome values

data = ["bob","ram","racecar","parth","naman"]

dict1 = {i for i in data if i == i[::-1]}

print(dict1)