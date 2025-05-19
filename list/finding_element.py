data = ['kalp', 'vidhi', 'hash', 'vatsal', 'jenil']

flag = -1

for i in range(len(data)):
    if data[i] == 'vidhi':
        flag = i
        break

print(flag)