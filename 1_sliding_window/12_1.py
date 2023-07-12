def words_concat(s, words):
    ws = 0
    wf = {}
    indexes = []
    matching = 0

    for w in words:
        if w not in wf:
            wf[w] = 0
        wf[w] += 1

    for we in range(len(words[0]), len(s)+len(words[0]), len(words[0])):
        print(s[ws:we])
        rw = s[we-len(words[0]):we]
        if rw in wf:
            wf[rw] -= 1
            if wf[rw] == 0:
                matching += 1

        if matching == len(wf):
            indexes.append(ws)

        if we >= len(words)*len(words[0]):
            lw = s[ws:ws+len(words[0])]
            ws += len(words[0])
            if lw in wf:
                if wf[lw] == 0:
                    matching -= 1
                wf[lw] += 1

    return indexes


s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
print(words_concat(s, words))
