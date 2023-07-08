def long_substr_no_rep(string):
    window_start = 0
    char_freq = {}
    max_len = 0

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while char_freq[right_char] > 1:
            left_char = string[window_start]
            char_freq[left_char] -= 1
            window_start += 1


        max_len = max(max_len, window_end - window_start + 1)

    return max_len

#print(long_substr_no_rep("abccde"))

def long_substr_no_rep_2(string):
    window_start = 0
    char_index = {}
    max_len = 0

    for window_end in range(len(string)):
        right_char = string[window_end]

        if right_char in char_index:
            window_start = max(window_start, char_index[right_char] + 1)

        char_index[right_char] = window_end

        max_len = max(max_len, window_end - window_start + 1)

    return max_len

print(long_substr_no_rep_2("abbbb"))
