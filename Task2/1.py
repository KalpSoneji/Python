# result = find_pairs([1, 2, 3, 4, 5, 6], 7)
# print(result)  # Output: [(3, 4), (2, 5), (1, 6)]


def find_pairs(list):
    result = []
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == 7:
                result.append((list[i], list[j]))
    return result

list = [1, 2, 3, 4, 5, 6]

ans = find_pairs(list)
print(ans)