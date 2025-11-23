
# READ DATA
with open('./2024/07.txt', 'r', encoding='utf-8') as f:
    INPUT = f.read()

# Procesar cada línea
lines = INPUT.strip().split('\n')
data = []
for line in lines:
    # Separar por ":"
    parts = line.split(':')
    result = int(parts[0].strip())  # Parte antes de ":"
    numbers = parts[1].strip().split()  # Parte después de ":" separada por espacios
    numbers = [int(num) for num in numbers]  # Convertir a enteros
    data.append((result, numbers))

# Función para probar todas las combinaciones de operadores
from itertools import product

def test_combinations(target, numbers):
    """Prueba todas las combinaciones de + y * de izquierda a derecha"""
    if len(numbers) == 1:
        return numbers[0] == target
    
    # Necesitamos len(numbers)-1 operadores
    num_operators = len(numbers) - 1
    
    # Generar todas las combinaciones de operadores (+ y *)
    for operators in product(['+', '*'], repeat=num_operators):
        # Evaluar de izquierda a derecha
        result = numbers[0]
        for i, op in enumerate(operators):
            if op == '+':
                result += numbers[i + 1]
            else:  # op == '*'
                result *= numbers[i + 1]
        
        if result == target:
            return True
    
    return False

def test_combinations_with_concat(target, numbers):
    """Prueba todas las combinaciones de +, * y concatenación de izquierda a derecha"""
    if len(numbers) == 1:
        return numbers[0] == target
    
    # Necesitamos len(numbers)-1 operadores
    num_operators = len(numbers) - 1
    
    # Generar todas las combinaciones de operadores (+, * y ||)
    for operators in product(['+', '*', '||'], repeat=num_operators):
        # Evaluar de izquierda a derecha
        result = numbers[0]
        for i, op in enumerate(operators):
            if op == '+':
                result += numbers[i + 1]
            elif op == '*':
                result *= numbers[i + 1]
            else:  # op == '||' (concatenación)
                result = int(str(result) + str(numbers[i + 1]))
        
        if result == target:
            return True
    
    return False

# DAY 7 PUZZLE 1
res1 = 0

for el in data:
    if test_combinations(el[0], el[1]):
        res1 += el[0]

print('DAY 7 PUZZLE 1:', res1)

# DAY 7 PUZZLE 2
res2 = 0

for el in data:
    if test_combinations_with_concat(el[0], el[1]):
        res2 += el[0]

print('DAY 7 PUZZLE 2: %d' % (res2))