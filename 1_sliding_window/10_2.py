def anagram_in_string(s, p):
    ws = 0
    pf = {}
    matching = 0
    indexes = []

    for c in p:
        if c not in pf:
            pf[c] = 0
        pf[c] += 1

    for we in range(len(s)):
        rc = s[we]
        if rc in pf:
            pf[rc] -= 1
            if pf[rc] == 0:
                matching += 1

        if matching == len(pf):
            indexes.append(ws)

        if we >= len(p) - 1:
            lc = s[ws]
            ws += 1
            if lc in pf:
                if pf[lc] == 0:
                    matching -= 1
                pf[lc] += 1

    return indexes


string = "abbcabc"
pattern = "abc"
print(anagram_in_string(string, pattern))
