import math

def small_substr(s, p):
    ws = 0
    pf = {}
    min_len = math.inf
    min_ws = 0
    contain = 0

    for c in p:
        if c not in pf:
            pf[c] = 0
        pf[c] += 1

    for we in range(len(s)):
        rc = s[we]
        if rc in pf:
            pf[rc] -= 1
            if pf[rc] == 0:
               contain += 1
        #print("contain:", contain)
        #print("pf:", pf)
        #if contain == len(pf):
        #    if we+1 < min_len:
        #        min_len = we+1
        #        min_ws = ws

        while contain >= len(pf):
            if contain == len(pf):
                if we-ws+1 < min_len:
                    min_len = we-ws+1
                    min_ws = ws

            lc = s[ws]
            ws += 1
            if lc in pf:
                if pf[lc] == 0:
                    contain -= 1
                pf[lc] += 1
            #if contain == len(pf):
            #    if we-ws+1 < min_len:
            #        min_len = we-ws+1
            #        min_ws = ws
    
    #print("min_ws:", min_ws)
    #print("min_len:", min_len)
    if min_len != math.inf:
        return s[min_ws:min_ws+min_len]
    return ""

string = "adcad"
pat = "abc"
print(small_substr(string, pat))

string = "abdabca"
pat = "abc"
print(small_substr(string, pat))

string = "aabdec"
pat = "abc"
print(small_substr(string, pat))

string = "abc"
pat = "abc"
print(small_substr(string, pat))


