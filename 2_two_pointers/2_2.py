def rem_key(arr, k):
    next_ele = 0
    for i in range(len(arr)):
        if arr[i] != k:
            arr[next_ele] = arr[i]
            next_ele += 1

    return next_ele

print(rem_key([3,2,3,6,3,10,9,3], 3))
print(rem_key([2, 11, 2, 2, 1], 2))
