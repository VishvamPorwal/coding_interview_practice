def max_num_fruits(fruits, b = 2):
    window_start = 0
    fruit_freq = {}
    max_len = 0
    
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        while len(fruit_freq) > b:
            left_fruit = fruits[window_start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            window_start += 1

        max_len = max(max_len, window_end - window_start + 1)

    return max_len

print(max_num_fruits(['A', 'B', 'C', 'B', 'B', 'C']))

        
