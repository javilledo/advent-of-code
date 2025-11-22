# READ DATA
INPUT = open('./2024/02.txt', 'r')
INPUT = [x.strip() for x in INPUT.readlines()]
INPUT = [x for x in INPUT]

# DAY 2 PUZZLE 1
res1 = 0
for informe in INPUT:
    informe_array = [int(x) for x in informe.split()]

    diferencias = [informe_array[i + 1] - informe_array[i] for i in range(len(informe_array) - 1)]
    
    if (all(num >= 1 for num in diferencias)) and (all(num <=3 for num in diferencias)): res1 +=1
    if (all(num <=-1 for num in diferencias)) and (all(num >=-3 for num in diferencias)): res1 +=1

print('DAY 2 PUZZLE 1: %d' % (res1))

# DAY 2 PUZZLE 2

def is_safe(arr):
    diffs = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    return (all(1 <= x <= 3 for x in diffs) or all(-3 <= x <= -1 for x in diffs))

res2 = 0
for informe in INPUT:
    informe_array = [int(x) for x in informe.split()]
    
    if is_safe(informe_array):
        res2 += 1
    else:
        for i in range(len(informe_array)):
            temp_array = informe_array[:i] + informe_array[i+1:]
            if is_safe(temp_array):
                res2 += 1
                break

print('DAY 2 PUZZLE 2: %d' % (res2))
