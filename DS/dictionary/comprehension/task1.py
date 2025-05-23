list = ["madam", "racecar", "amit", "bob"]

dict = {l : "yes" if l == l[::-1] else "no" for l in list}

print(dict)

numbers = [121,222,34,56,789,111,90,434]

dict1 = {i : "yes" if str(i) == str(i)[::-1] else "no" for i in numbers}

print(dict1)