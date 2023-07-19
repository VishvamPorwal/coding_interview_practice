def sorted_rem_dup(arr):
    next_non_dup = 1
    i = 1

    while(i < len(arr)):
        if arr[next_non_dup - 1] != arr[i]:
            arr[next_non_dup] = arr[i]
            next_non_dup += 1

        i += 1

    return next_non_dup

print(sorted_rem_dup([2, 3, 3, 3, 6, 9, 9]))
print(sorted_rem_dup([2, 2, 2, 11]))
