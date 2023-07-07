import math

def smallest_contg_subarr_sum_greater_than_s(s, arr):
    window_start = 0
    min_length = math.inf
    window_sum = 0.0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            print(f"min_len:{min_length}, window_start:{window_start}, window_end:{window_end}, window_sum: {window_sum}")
            window_sum -= arr[window_start]
            window_start += 1

smallest_contg_subarr_sum_greater_than_s(8, [3,4,1,1,6])
