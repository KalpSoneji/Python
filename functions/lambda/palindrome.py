users = ["naman", "madam", "chaman", "raj"]

def palindrome(x):
    flag = True

    for i in x:
        if i[::] != i[::-1]:
            flag = False

        return flag
    
test = lambda x: palindrome(x)

print(test(users))