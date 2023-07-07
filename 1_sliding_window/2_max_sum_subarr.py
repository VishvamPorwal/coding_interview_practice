def max_sum_subarr(k, arr):
    max_sum = 0.0
    cur_sum = 0.0
    window_start = 0
    
    for window_end in range(len(arr)):
        cur_sum += arr[window_end]

        if window_end >= k-1:
            if cur_sum > max_sum:
                max_sum = cur_sum
            cur_sum -= arr[window_start]
            window_start += 1

        print(f"cur_sum:{cur_sum+arr[window_start-1]}, max_sum:{max_sum}, window_start:{window_start-1}, window_end: {window_end}")

max_sum_subarr(2, [2,3,4,1,5])
