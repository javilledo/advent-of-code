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
res2 = 0
for informe in INPUT:
    informe_array = [int(x) for x in informe.split()]
    trend = 0 # será 1 si creciente y -1 si decreciente
    previous_num = 0
    for i, num in enumerate(informe_array):
        if i == 0: previous_num = num
        if i > 0:
            dif_temp = num - previous_num
            if dif_temp > 0
            
    pass

print('DAY 2 PUZZLE 2: %d' % (res2))
