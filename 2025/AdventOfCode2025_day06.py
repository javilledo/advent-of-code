# READ DATA
raw_input = open('./2025/06.txt', 'r').read().splitlines()
matrix = [line.split() for line in raw_input]
INPUT = list(map(list, zip(*matrix)))


# DAY 6 PUZZLE 1
res1 = 0

for row in INPUT:
    operator = row[-1]
    numbers = [int(x) for x in row[:-1]]
    
    current_val = 0
    if operator == '+':
        current_val = sum(numbers)
    elif operator == '*':
        current_val = 1
        for num in numbers:
            current_val *= num
            
    res1 += current_val

print('DAY 6 PUZZLE 1: %d' % (res1))

# DAY 6 PUZZLE 2
res2 = 0

lines = raw_input
max_len = max(len(line) for line in lines)
padded_lines = [line.ljust(max_len) for line in lines]

rows = len(padded_lines)
cols = max_len

current_block_cols = []

def solve_block(block_cols_indices):
    if not block_cols_indices:
        return 0
    
    numbers = []
    operator = None
    
    for c in block_cols_indices:
        char_at_bottom = padded_lines[rows-1][c]
        if char_at_bottom in '+*':
            operator = char_at_bottom
            
        col_str = "".join(padded_lines[r][c] for r in range(rows-1))
        col_str = col_str.strip()
        if col_str:
            numbers.append(int(col_str))
            
    if not operator or not numbers:
        return 0
        
    val = 0
    if operator == '+':
        val = sum(numbers)
    elif operator == '*':
        val = 1
        for n in numbers:
            val *= n
    return val

for c in range(cols):
    is_empty = all(padded_lines[r][c] == ' ' for r in range(rows))
    
    if is_empty:
        if current_block_cols:
            res2 += solve_block(current_block_cols)
            current_block_cols = []
    else:
        current_block_cols.append(c)

if current_block_cols:
    res2 += solve_block(current_block_cols)

print('DAY 6 PUZZLE 2: %d' % (res2))    