# Return all elements that appear more than once.

# Input: [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]

def fnc(*args): 
    
    ans = []

    for num in args:
        if args.count(num) > 1 and num not in ans:
            ans.append(num)
    
    return ans

final = fnc(1, 2, 3, 4, 5, 6, 5, 4, 1, 7, 9, 8)

print(final)
