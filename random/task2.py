# generate a 5 character name

import random

x = chr(random.randint(ord('A'), ord('Z')))
print(x, end='')

for i in range(4):
    x = chr(random.randint(ord('a'), ord('z')))
    print(x, end='')
