def word_concat(s, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_freq = {}

    for word in words:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1

    result_indices = []
    words_count = len(words)
    word_len = len(words[0])

    for i in range((len(s) - words_count * word_len) + 1):
        words_seen = {}
        for j in range(0, words_count):
            ind = i + j * word_len
            word = s[ind: ind + word_len]

            if word not in word_freq:
                break
            
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

        if words_seen == word_freq:
            result_indices.append(i)

    return result_indices
        

s = "catfoxcatfox"
words = ["cat", "fox"]
print(word_concat(s, words))
