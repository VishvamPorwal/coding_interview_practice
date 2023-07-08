def anagrams_of_pat(s, p):
    window_start = 0
    anagrams = []
    pat_freq = {}
    char_freq = {}
    
    for c in p:
        if c not in pat_freq:
            pat_freq[c] = 0
        pat_freq[c] += 1
    
    print(pat_freq)

    for window_end in range(len(s)):
        rc = s[window_end]
        if rc not in char_freq:
            char_freq[rc] = 0
        char_freq[rc] += 1
        print(char_freq)
        if char_freq == pat_freq:
            anagrams.append(window_start)
        
        if window_end - window_start + 1 >= len(p):
            lc = s[window_start]
            char_freq[lc] -= 1
            if char_freq[lc] == 0:
                del char_freq[lc]
            window_start += 1

    return anagrams

st = "abbcabc"
pat = "abc"

print(anagrams_of_pat(st, pat))
