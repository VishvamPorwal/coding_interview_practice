def long_substr_same_after_replace(k, string):
    window_start = 0
    char_freq = {}
    max_count = 0
    max_len = 0
    
    for window_end in range(len(string)):
        print("window:",string[window_start:window_end+1])
        right_char = string[window_end]
        print("right_char:",right_char)

        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        print("char_freq:", char_freq)
        
        max_count = max(max_count, char_freq[right_char])

        if window_end - window_start + 1 - max_count > k:
            left_char = string[window_start]
            char_freq[left_char] -= 1
            window_start += 1
            print("new_window:", string[window_start: window_end+1])
            print("new_char_freq:", char_freq)
        
        max_len = max(max_len, window_end - window_start + 1)
        print("max_len:",max_len)
        print()

    return max_len

k = 2
str_inp = "BAAAB"
print(k, str_inp)
print(long_substr_same_after_replace(k, str_inp))
