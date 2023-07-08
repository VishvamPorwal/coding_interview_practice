def perm_in_str(s, p):
    window_start = 0
    pat_freq = {}
    char_freq = {}

    for c in p:
        if c not in pat_freq:
            pat_freq[c] = 0
        pat_freq[c] += 1

    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char not in char_freq:
            char_freq[right_char] = 0
        char_freq[right_char] += 1
        
        if pat_freq == char_freq:
            return True
        elif (window_end - window_start + 1) >= len(p):
            left_char = s[window_start]
            char_freq[left_char] -= 1
            if char_freq[left_char] == 0:
                del char_freq[left_char]
            window_start += 1
    return False

pat = "abc"
string = "aaacb"

print(perm_in_str(string, pat))
