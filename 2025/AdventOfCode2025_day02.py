# READ DATA
INPUT = open('./2025/02.txt', 'r')
content = INPUT.read().strip()
if content.endswith('.'):
    content = content[:-1]
INPUT = [[int(val) for val in x.split('-')] for x in content.split(',')]

# DAY 2 PUZZLE 1
res1 = 0

def is_repetitive(n):
    s = str(n)
    length = len(s)
    if length % 2 == 0:
        half = length // 2
        substring = s[:half]
        if substring * 2 == s:
            return True
    return False

for pair in INPUT:
    start, end = pair
    for num in range(start, end + 1):
        if is_repetitive(num):
            res1 += num
            
print('DAY 2 PUZZLE 1: %d' % (res1))

# DAY 2 PUZZLE 2
res2 = 0

def is_repetitive_any(n):
    s = str(n)
    length = len(s)
    for l in range(1, length // 2 + 1):
        if length % l == 0:
            substring = s[:l]
            repetitions = length // l
            if substring * repetitions == s:
                return True
    return False

for pair in INPUT:
    start, end = pair
    for num in range(start, end + 1):
        if is_repetitive_any(num):
            res2 += num

print('DAY 2 PUZZLE 2: %d' % (res2))