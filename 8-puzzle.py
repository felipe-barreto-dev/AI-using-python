import heapq

# Estado objetivo (solução final)
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # O 0 representa o espaço vazio
]

# Função que calcula a distância de Manhattan (heurística)
def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:  # Ignora o espaço vazio
                goal_i, goal_j = [(goal_x, goal_y) for goal_x in range(3) for goal_y in range(3) if goal[goal_x][goal_y] == value][0]
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance

# Função que encontra a posição do espaço vazio (0)
def find_empty_space(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Função que gera novos estados movendo o espaço vazio
def generate_neighbors(state):
    neighbors = []
    x, y = find_empty_space(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Cima, Baixo, Esquerda, Direita
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            # Cria uma cópia do estado atual e troca o 0 com a nova posição
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    
    return neighbors

# Função que resolve o quebra-cabeça usando o algoritmo A*
def solve_puzzle(start_state):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_state, []))  # (Custo, Estado, Caminho)
    visited = set()  # Usado para evitar revisitar estados
    
    while priority_queue:
        cost, current_state, path = heapq.heappop(priority_queue)
        
        if current_state == goal_state:  # Verifica se o estado atual é o objetivo
            return path + [current_state]  # Retorna o caminho completo
        
        visited.add(tuple(map(tuple, current_state)))  # Marca o estado como visitado
        
        # Gera os vizinhos (próximos estados) e os adiciona à fila
        for neighbor in generate_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                new_cost = cost + 1
                heuristic = manhattan_distance(neighbor, goal_state)
                heapq.heappush(priority_queue, (new_cost + heuristic, neighbor, path + [current_state]))

    return None  # Caso nenhuma solução seja encontrada

# Estado inicial do quebra-cabeça
start_state = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

# Resolver o quebra-cabeça
solution = solve_puzzle(start_state)

# Mostrar a solução encontrada
if solution:
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("Nenhuma solução encontrada.")
