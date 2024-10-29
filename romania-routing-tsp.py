import itertools

# Grafo representando as distâncias entre as cidades na Romênia
romania_graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Rimnicu': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route)):
        city_from = route[i]
        city_to = route[(i + 1) % len(route)]  # Usar o módulo para retornar à cidade de origem
        total_distance += romania_graph[city_from].get(city_to, float('inf'))  # Usar get para evitar KeyError
    return total_distance

def tsp_dynamic_programming(cities):
    n = len(cities)
    memo = {}
    
    # Função recursiva com memoização
    def visit(city, visited):
        if (city, visited) in memo:
            return memo[(city, visited)]
        
        # Se todos foram visitados, retornar à cidade de origem
        if visited == (1 << n) - 1:
            return romania_graph[cities[city]].get(cities[0], float('inf'))  # Retornar ao ponto inicial
        
        min_cost = float('inf')
        
        # Iterar por todas as cidades
        for next_city in range(n):
            if visited & (1 << next_city) == 0:  # Se a cidade não foi visitada
                cost = romania_graph[cities[city]].get(cities[next_city], float('inf'))
                total_cost = cost + visit(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, total_cost)

        memo[(city, visited)] = min_cost
        return min_cost
    
    # Iniciar a busca a partir da primeira cidade
    return visit(0, 1)

# Lista de cidades
cities = list(romania_graph.keys())

# Executando o algoritmo
min_distance = tsp_dynamic_programming(cities)

print("Distância mínima:", min_distance, "km")
