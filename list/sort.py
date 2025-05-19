data = ['kalp', 'vidhi', 'hash', 'vatsal', 'jenil']

data.reverse()
print(data)

data.sort() #sorts alphabetically
print(data)

data.sort(key=len) #sorts acc to length
print(data)

data.sort(key=len, reverse=True) #sorts acc to length then reverses it
print(data)