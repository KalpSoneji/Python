#elements starting with s should be put into a new list

data = ['sam', "shyam", 'ram', 'hari', 'seeta']
s = []

# for i in data:
#     if i.startswith('s'):
#         s.append(i)

for i in data:
    if i[0] == 's':
        s.append(i)

print(s)