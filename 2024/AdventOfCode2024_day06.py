
# READ DATA
with open('./2024/06.txt', 'r', encoding='utf-8') as f:
    INPUT = f.read()

# Convert INPUT to a matrix (list of lists)
INPUT = INPUT.split('\n')
INPUT = [list(row) for row in INPUT if row.strip()]

# Definir los movimientos según la dirección
directions = {
    '^': [-1, 0],  # arriba
    'v': [1, 0],   # abajo
    '<': [0, -1],  # izquierda
    '>': [0, 1]    # derecha
}

# Definir rotación 90º a la derecha
rotation_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

# DAY 6 PUZZLE 1
res1 = set()  # Usar set para almacenar posiciones únicas

# Encontrar la posición del caracter que indica la dirección (^, <, >, v)
current_pos = None
direction = None
for i in range(len(INPUT)):
    for j in range(len(INPUT[i])):
        if INPUT[i][j] in ['^', '<', '>', 'v']:
            current_pos = [i, j]
            direction = INPUT[i][j]
            res1.add((i, j))  # Agregar la posición inicial como tupla
            break
    if current_pos:  # Exit outer loop if found
        break

# Guardar posición y dirección inicial para el puzzle 2
initial_pos = current_pos.copy()
initial_direction = direction

# Mover el carácter hasta salir de la matriz
while True:
    # Calcular la siguiente posición
    delta = directions[direction]
    next_row = current_pos[0] + delta[0]
    next_col = current_pos[1] + delta[1]
    
    # Verificar si la siguiente posición está fuera de los límites
    if next_row < 0 or next_row >= len(INPUT) or next_col < 0 or next_col >= len(INPUT[0]):
        break  # Salir si está fuera de la matriz
    
    # Verificar si la siguiente posición es un obstáculo
    if INPUT[next_row][next_col] == '#':
        # Girar 90º a la derecha
        direction = rotation_right[direction]
    else:
        # Mover a la siguiente posición
        current_pos = [next_row, next_col]
        res1.add((next_row, next_col))  # Agregar como tupla al set

res1 = len(res1)
print('DAY 6 PUZZLE 1:', res1)

# DAY 6 PUZZLE 2
res2 = 0

# Función para simular el recorrido y detectar si hay bucle infinito
def simulate_with_obstacle(matrix, obstacle_pos, start_pos, start_dir):
    """
    Simula el recorrido del guardia con un obstáculo adicional.
    Retorna True si el guardia entra en un bucle infinito, False si sale de la matriz.
    """
    current_pos = start_pos.copy()
    direction = start_dir
    
    # Rastrear estados (posición + dirección) para detectar bucles
    visited_states = set()
    visited_states.add((current_pos[0], current_pos[1], direction))
    
    while True:
        # Calcular la siguiente posición
        delta = directions[direction]
        next_row = current_pos[0] + delta[0]
        next_col = current_pos[1] + delta[1]
        
        # Verificar si la siguiente posición está fuera de los límites
        if next_row < 0 or next_row >= len(matrix) or next_col < 0 or next_col >= len(matrix[0]):
            return False  # Sale de la matriz, no hay bucle
        
        # Verificar si la siguiente posición es un obstáculo (original o nuevo)
        is_obstacle = (matrix[next_row][next_col] == '#') or ([next_row, next_col] == obstacle_pos)
        
        if is_obstacle:
            # Girar 90º a la derecha
            direction = rotation_right[direction]
        else:
            # Mover a la siguiente posición
            current_pos = [next_row, next_col]
        
        # Crear el estado actual (posición + dirección)
        state = (current_pos[0], current_pos[1], direction)
        
        # Si ya visitamos este estado, hay un bucle infinito
        if state in visited_states:
            return True  # Bucle infinito detectado
        
        visited_states.add(state)

# Probar colocar un obstáculo en cada posición de la matriz
for i in range(len(INPUT)):
    for j in range(len(INPUT[0])):
        # No colocar obstáculo en la posición inicial del guardia
        if [i, j] == initial_pos:
            continue
        
        # No colocar obstáculo donde ya hay uno
        if INPUT[i][j] == '#':
            continue
        
        # Simular con un obstáculo en la posición [i, j]
        if simulate_with_obstacle(INPUT, [i, j], initial_pos, initial_direction):
            res2 += 1

print('DAY 6 PUZZLE 2: %d' % (res2))