def permut_in_str(s, p):
    pat_freq = {}
    ws = 0
    matching = 0

    for c in p:
        if c not in pat_freq:
            pat_freq[c] = 0
        pat_freq[c] += 1

    for we in range(len(s)):
        rc = s[we]
        if rc in pat_freq:
            pat_freq[rc] -= 1
            if pat_freq[rc] == 0:
                matching += 1

        if matching == len(pat_freq):
            return True

        if we >= len(p) - 1:
            lc = s[ws]
            ws += 1
            if lc in pat_freq:
                if pat_freq[lc] == 0:
                    matching -= 1
                pat_freq[lc] += 1

    return False

string = "bcdxabcdy"
pattern = "bcdyabcdx"

print(permut_in_str(string, pattern))
