# READ DATA
INPUT = open('./2025/01.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

# DAY 1 PUZZLE 1

res1 = 0
pos = 50

for instruction in INPUT:

    direction = instruction[0]
    magnitude = int(instruction[1:])
    
    if direction == 'R':
        pos = (pos + magnitude) % 100
    elif direction == 'L':
        pos = (pos - magnitude) % 100
    
    if pos == 0: res1 += 1
    
print('DAY 1 PUZZLE 1: %d' % (res1))

# DAY 1 PUZZLE 2

res2 = 0
pos = 50

for instruction in INPUT:
    direction = instruction[0]
    magnitude = int(instruction[1:])
    
    if direction == 'R':
        start = pos
        end = pos + magnitude
        res2 += end // 100 - start // 100
        
        pos = (pos + magnitude) % 100
        
    elif direction == 'L':
        start = pos
        end = pos - magnitude
        res2 += (start - 1) // 100 - (end - 1) // 100
        
        pos = (pos - magnitude) % 100
    
print('DAY 1 PUZZLE 2: %d' % (res2))