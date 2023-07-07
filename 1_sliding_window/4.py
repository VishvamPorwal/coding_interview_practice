def longest_substr(k, string):
    window_start = 0
    char_freq = {}
    max_len = 0

    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1

        while len(char_freq) > k:
            left_char = string[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len

print(longest_substr(1, "araaci"))
