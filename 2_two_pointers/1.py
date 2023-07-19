def sorted_target_sum(arr, t):
    left, right = 0, len(arr) - 1
    while(left < right):
        cur_sum = arr[left] + arr[right]
        if cur_sum == t:
            return [left, right]
        if cur_sum > t:
            right -= 1
        else:
            left += 1

    return [-1, -1]

print(sorted_target_sum([1,2,3,4,6], 6))
print(sorted_target_sum([2, 5, 9, 11], 11))
