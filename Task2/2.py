# Rotate a list to the right by k steps.

# Input: [1, 2, 3, 4, 5], k=2
# Output: [4, 5, 1, 2, 3]

list = [1, 2, 3, 4, 5]

k = int(input("Enter a number: "))

k = k % len(list)

ans = list[-k:] + list[:-k]

print(ans)