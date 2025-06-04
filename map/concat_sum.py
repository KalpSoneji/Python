no1 = [1, 2, 3]
no2 = [4, 5, 6]

sum = list(map(lambda x, y : x + y, no1, no2))

print(sum)

fname = ["amitabh", "hrithik", "ajay"]
lname = ["Bachchan", "roshan", "devgn"]

name = tuple(map(lambda x, y : x.title() + " " + y.capitalize(), fname, lname))

print(name)