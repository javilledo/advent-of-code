# READ DATA
raw_input = open('./2025/07.txt', 'r').read().splitlines()
INPUT = [list(line) for line in raw_input]
print(INPUT)

# DAY 7 PUZZLE 1
res1 = 0
rows = len(INPUT)
cols_len = len(INPUT[0])

start_pos = None
for r in range(rows):
    for c in range(cols_len):
        if INPUT[r][c] == 'S':
            start_pos = (r, c)
            break
    if start_pos: break

if start_pos:
    current_cols = {start_pos[1]}
    
    # Iterate from start row to second to last row
    for r in range(start_pos[0], rows - 1):
        next_cols = set()
        for c in current_cols:
            # Look ahead at r+1
            target_char = INPUT[r+1][c]
            
            if target_char == '^':
                res1 += 1
                # Split
                if c > 0:
                    next_cols.add(c-1)
                    if INPUT[r+1][c-1] == '.': INPUT[r+1][c-1] = '|'
                if c < cols_len - 1:
                    next_cols.add(c+1)
                    if INPUT[r+1][c+1] == '.': INPUT[r+1][c+1] = '|'
            else:
                # Continue
                next_cols.add(c)
                if INPUT[r+1][c] == '.':
                    INPUT[r+1][c] = '|'
        
        current_cols = next_cols

print('DAY 7 PUZZLE 1: %d' % (res1))

# DAY 7 PUZZLE 2
res2 = 0
dp = [[0] * cols_len for _ in range(rows)]

if start_pos:
    dp[start_pos[0]][start_pos[1]] = 1
    
    for r in range(start_pos[0], rows - 1):
        for c in range(cols_len):
            if dp[r][c] > 0:
                target_char = INPUT[r+1][c]
                if target_char == '^':
                    # Split
                    if c > 0:
                        dp[r+1][c-1] += dp[r][c]
                    if c < cols_len - 1:
                        dp[r+1][c+1] += dp[r][c]
                else:
                    # Straight
                    dp[r+1][c] += dp[r][c]

    res2 = sum(dp[rows-1])

print('DAY 7 PUZZLE 2: %d' % (res2))        