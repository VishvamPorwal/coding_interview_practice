def sorted_target_sum(arr, t):
    seen = {}
    for i in range(len(arr)):
        x = arr[i]
        if t-x in seen:
            return [seen[t-x], i]
        else:
            seen[x] = i

    return [-1, -1]

print(sorted_target_sum([1, 2, 3, 4, 6], 6))
print(sorted_target_sum([2, 5, 9, 11], 11))
