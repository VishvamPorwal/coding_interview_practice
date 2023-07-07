def calc_contg_avg(k, arr):
    window_sum = 0.0
    window_start = 0
    result = []
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= k-1:
            result.append(window_sum/k)
            window_sum -= arr[window_start]
            window_start+=1
        print(f"window_sum:{window_sum}, window_start:{window_start}, window_end:{window_end}, result:{result}")


calc_contg_avg(5, [1,3,2,6,-1,4,1,8,2])

