def square_sort(arr):
    res = [0] * len(arr)
    left = 0
    right = len(arr) - 1
    biggest = right

    while left <= right:
        left_sq = arr[left] ** 2
        right_sq = arr[right] ** 2
        
        #print("init:", arr[left: right + 1])

        if left_sq > right_sq:
            res[biggest] = left_sq
            left += 1
        else:
            res[biggest] = right_sq
            right -= 1

        biggest -= 1
        #print("later:",arr[left: right + 1])
        #print("res:", res)


    return res

print(square_sort([-2, -1, 1, 2, 3]))
print(square_sort([-2, -1, 0, 2, 3]))
print(square_sort([-3, -1, 0, 1, 2]))
