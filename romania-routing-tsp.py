import random
import numpy as np

# Definindo o grafo das cidades na Romênia e suas distâncias
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

# Função para calcular a distância total de uma rota
def calculate_distance(route, graph):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]].get(route[i + 1], float('inf'))
    # Retornar à cidade de origem
    total_distance += graph[route[-1]].get(route[0], float('inf'))
    return total_distance

# Função para gerar uma rota aleatória
def generate_route(cities):
    route = cities[:]
    random.shuffle(route)
    return route

# Função para gerar a população inicial de rotas
def generate_population(population_size, cities):
    return [generate_route(cities) for _ in range(population_size)]

# Função de crossover (combinar dois pais para criar uma nova rota)
def crossover(parent1, parent2):
    size = len(parent1)
    start = random.randint(0, size - 2)
    end = random.randint(start, size - 1)
    child = [None] * size
    child[start:end] = parent1[start:end]

    # Preencher o restante do filho com genes do segundo pai
    current_position = end
    for gene in parent2:
        if gene not in child:
            if current_position >= size:
                current_position = 0
            child[current_position] = gene
            current_position += 1

    return child

# Função de mutação (trocar duas cidades aleatoriamente)
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Seleção de pais (torneio)
def select_parents(population, graph, tournament_size):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda route: calculate_distance(route, graph))
    return tournament[0], tournament[1]

# Algoritmo Genético
def genetic_algorithm(graph, population_size=100, generations=500, mutation_rate=0.01, tournament_size=5):
    cities = list(graph.keys())
    population = generate_population(population_size, cities)
    best_route = min(population, key=lambda route: calculate_distance(route, graph))
    best_distance = calculate_distance(best_route, graph)

    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, graph, tournament_size)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        current_best_route = min(population, key=lambda route: calculate_distance(route, graph))
        current_best_distance = calculate_distance(current_best_route, graph)

        if current_best_distance < best_distance:
            best_route = current_best_route
            best_distance = current_best_distance

    return best_route, best_distance

# Executar o algoritmo genético
best_route, best_distance = genetic_algorithm(romania_graph)

# Exibir os resultados
print(f"Melhor rota: {' -> '.join(best_route)}")
print(f"Distância total: {best_distance} km")
