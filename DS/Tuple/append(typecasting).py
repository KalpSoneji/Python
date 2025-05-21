tdata = (1, 2, 3) #creating tuple

ldata = list(tdata) #typecasting tuple to list

ldata.append(4); #appending element

tdata = tuple(ldata) #typecasting back to tuple

print(tdata)

x = (1, 2, 3)
y = (4, 5, 6)
z = x + y

print(z)