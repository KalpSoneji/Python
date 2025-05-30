dict = {"a" : 90, "b" : 70, "c" : 80}

max = max(dict.values())

for name, marks in dict.items():
    if max == marks:
        print(name)