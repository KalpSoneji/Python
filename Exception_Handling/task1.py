# # try to access out of index in string, array 

# str = "ram"

# try:
#     print(str[5])

# except IndexError as e:
#     print("Particular", e)

list = [1, 2,  3]

try:
    print(list[5])

except IndexError as e:
    print("Particular", e)

finally:
    print("EOF")