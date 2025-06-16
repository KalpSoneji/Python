# Use sets to find elements common in both lists.

# Input: [1, 2, 3], [2, 3, 4]
# Output: {2, 3}

list1 = [1, 2, 3]
list2 = [2, 3, 4]

set1 = set(list1)
set2 = set(list2)

ans = set1.intersection(set2)

print(ans)
