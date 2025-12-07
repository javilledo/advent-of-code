# READ DATA
INPUT = open('./2025/04.txt', 'r').read().splitlines()
INPUT = [list(line) for line in INPUT]

# DAY 4 PUZZLE 1
res1 = 0
rows = len(INPUT)
cols = len(INPUT[0])

for r in range(rows):
    for c in range(cols):
        if INPUT[r][c] == '@':
            neighbors = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if INPUT[nr][nc] == '@':
                            neighbors += 1
            if neighbors < 4:
                res1 += 1

print('DAY 4 PUZZLE 1: %d' % (res1))

# DAY 4 PUZZLE 2
res2 = 0
while True:
    changes = []
    for r in range(rows):
        for c in range(cols):
            if INPUT[r][c] == '@':
                neighbors = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols:
                            if INPUT[nr][nc] == '@':
                                neighbors += 1
                if neighbors < 4:
                    changes.append((r, c))
    
    if not changes:
        break
    
    res2 += len(changes)
    for r, c in changes:
        INPUT[r][c] = '.'

print('DAY 4 PUZZLE 2: %d' % (res2))    