import re

# READ DATA
with open('./2024/03.txt', 'r', encoding='utf-8') as f:
    INPUT = f.read().replace('\n', '')

# DAY 3 PUZZLE 1
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, INPUT)
res1 = 0
for match in matches:
    res1 += int(match[0]) * int(match[1])

print('DAY 3 PUZZLE 1: %d' % (res1))

# DAY 3 PUZZLE 2
pattern2 = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
matches2 = re.findall(pattern2, INPUT)

res2 = 0
enabled = True
for match in matches2:
    instruction = match[0]
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    elif instruction.startswith("mul("):
        if enabled:
            res2 += int(match[1]) * int(match[2])

print('DAY 3 PUZZLE 2: %d' % (res2))
