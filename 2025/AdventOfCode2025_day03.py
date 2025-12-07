# READ DATA
INPUT = open('./2025/03.txt', 'r').read().splitlines()

# DAY 3 PUZZLE 1

res1 = 0
for line in INPUT:
    max_val = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            val = int(line[i] + line[j])
            if val > max_val:
                max_val = val
    res1 += max_val

print('DAY 3 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2
res2 = 0

def get_max_subsequence(line, length):
    current_idx = 0
    digits_to_pick = length
    result = []
    
    while digits_to_pick > 0:
        search_end = len(line) - digits_to_pick + 1
        window = line[current_idx : search_end]
        
        max_digit = max(window)
        
        occurrence_in_window = window.index(max_digit)
        absolute_idx = current_idx + occurrence_in_window
        occurrence_in_window = window.index(max_digit)
        absolute_idx = current_idx + occurrence_in_window
        
        result.append(max_digit)
        current_idx = absolute_idx + 1
        digits_to_pick -= 1
        
    return int("".join(result))

for line in INPUT:
    res2 += get_max_subsequence(line, 12)

print('DAY 3 PUZZLE 2: %d' % (res2))    