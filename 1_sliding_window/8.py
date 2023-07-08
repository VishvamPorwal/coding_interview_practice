def longest_1s(k, s):
    window_start = 0
    max_len = 0
    bin_freq = {
            0:0,
            1:0
            }

    for window_end in range(len(s)):
        right_char = s[window_end]
        bin_freq[right_char] += 1

        if window_end - window_start + 1 - bin_freq[1] > k:
            left_char = s[window_start]
            bin_freq[left_char] -= 1
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len

print(longest_1s(3,[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]))
