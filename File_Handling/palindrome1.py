names = ['bob', 'john', 'ram', 'shyam', 'naman', 'parth', 'madam', 'java', 'python']

with open("./File_Handling/names.txt", 'w') as f:
    for name in names:
        f.write(name + '\n')

with open("./File_Handling/names.txt", 'r') as f, open("./File_Handling/pal_names.txt", 'w') as wf:
    for line in f:
        name = line.strip()
        if name == name[::-1]:
            wf.write(name + '\n')