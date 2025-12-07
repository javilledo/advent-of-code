# READ DATA
raw_input = open('./2025/05.txt', 'r').read()
parts = raw_input.strip().split('\n\n')

INPUT_01 = []
for line in parts[0].splitlines():
    INPUT_01.append([int(x) for x in line.split('-')])

INPUT_02 = [int(x) for x in parts[1].splitlines()]


# DAY 5 PUZZLE 1
res1 = 0

for num in INPUT_02:
    for start, end in INPUT_01:
        if start <= num <= end:
            res1 += 1
            break

print('DAY 5 PUZZLE 1: %d' % (res1))

# DAY 5 PUZZLE 2
ranges = sorted(INPUT_01, key=lambda x: x[0])
merged_ranges = []

if ranges:
    curr_start, curr_end = ranges[0]
    for i in range(1, len(ranges)):
        next_start, next_end = ranges[i]
        
        if next_start <= curr_end + 1:
            curr_end = max(curr_end, next_end)
        else:
            merged_ranges.append((curr_start, curr_end))
            curr_start, curr_end = next_start, next_end
    merged_ranges.append((curr_start, curr_end))

res2 = sum(end - start + 1 for start, end in merged_ranges)

print('DAY 5 PUZZLE 2: %d' % (res2))    