def search_triplets(arr):
    arr.sort()
    #print(f"{arr=}")
    triplets = []
    right = len(arr) - 1

    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        search_pairs(triplets, -arr[i], right, i+1, arr)

    return triplets


def search_pairs(triplets, target_sum, right, left, arr):
    while left < right:
        #print(f"{arr[left: right+1]=}")
        cur_sum = arr[left] + arr[right]
        #print(f"{cur_sum=}")
        #print(f"{target_sum=}")
        #print(arr[left], arr[right])
        if cur_sum == target_sum:
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right+1]:
                right -= 1
        elif cur_sum < target_sum:
            left += 1
        else:
            right -= 1


print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
print(search_triplets([-5, 2, -1, -2, 3]))
