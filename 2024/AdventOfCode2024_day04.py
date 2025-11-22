
# READ DATA
with open('./2024/04.txt', 'r', encoding='utf-8') as f:
    INPUT = f.read()

# DAY 4 PUZZLE 1
res1 = 0
grid = INPUT.strip().split('\n')
rows = len(grid)
cols = len(grid[0])
target = "XMAS"
target_len = len(target)

directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right
    (1, -1),  # Down-Left
    (-1, 1),  # Up-Right
    (-1, -1)  # Up-Left
]

for r in range(rows):
    for c in range(cols):
        for dr, dc in directions:
            found = True
            for i in range(target_len):
                nr, nc = r + dr * i, c + dc * i
                if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target[i]):
                    found = False
                    break
            if found:
                res1 += 1

print('DAY 4 PUZZLE 1: %d' % (res1))

# DAY 4 PUZZLE 2
res2 = 0

# Buscar patrones X-MAS: la 'A' está en el centro
# y en las dos diagonales debe haber "MAS" o "SAM"
for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if grid[r][c] == 'A':
            # Verificar diagonal principal (arriba-izq a abajo-der)
            diag1 = grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1]
            # Verificar diagonal secundaria (arriba-der a abajo-izq)
            diag2 = grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1]
            
            # Ambas diagonales deben ser "MAS" o "SAM"
            if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
                res2 += 1

print('DAY 4 PUZZLE 2: %d' % (res2))