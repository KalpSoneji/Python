#make a dictionary of their initials
#make a unique dictionary, ignore case sensitivity

cities = ["Ahmedabad","Surat","Anand","Rajkot","Somnath","Baroda", "baroda", "rajkot"]

# dict = {i[0] for i in cities}

# print(dict)

dict = {i.capitalize() for i in cities}

print(dict)