import random
import numpy as np

# Definindo as cidades na Romênia e suas distâncias (matriz de distâncias)
cities = ["Arad", "Bucharest", "Craiova", "Drobeta", "Eforie", "Fagaras", "Giurgiu", "Hirsova", "Iasi", "Lugoj", "Mehadia", "Neamt", "Oradea", "Pitesti", "Rimnicu", "Sibiu", "Timisoara", "Urziceni", "Vaslui", "Zerind"]

# Matriz de distâncias entre as cidades (exemplo simplificado, distância aleatória entre 100-500 km)
distances = np.random.randint(100, 500, size=(len(cities), len(cities)))

# Função para calcular a distância total de uma rota
def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i + 1]]
    # Retornar à cidade de origem
    total_distance += distances[route[-1]][route[0]]
    return total_distance

# Função para gerar uma rota aleatória
def generate_route(cities):
    route = random.sample(range(len(cities)), len(cities))
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
    index = 0
    for gene in parent2:
        if gene not in child:
            while child[index] is not None:
                index += 1
            child[index] = gene

    return child

# Função de mutação (trocar duas cidades aleatoriamente)
def mutate(route, mutation_rate):
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route) - 1)
            route[i], route[j] = route[j], route[i]
    return route

# Seleção de pais (torneio)
def select_parents(population, distances, tournament_size):
    tournament = random.sample(population, tournament_size)
    tournament.sort(key=lambda route: calculate_distance(route, distances))
    return tournament[0], tournament[1]

# Algoritmo Genético
def genetic_algorithm(cities, distances, population_size=100, generations=500, mutation_rate=0.01, tournament_size=5):
    population = generate_population(population_size, cities)
    best_route = min(population, key=lambda route: calculate_distance(route, distances))
    best_distance = calculate_distance(best_route, distances)

    for _ in range(generations):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = select_parents(population, distances, tournament_size)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population
        current_best_route = min(population, key=lambda route: calculate_distance(route, distances))
        current_best_distance = calculate_distance(current_best_route, distances)

        if current_best_distance < best_distance:
            best_route = current_best_route
            best_distance = current_best_distance

    return best_route, best_distance

# Executar o algoritmo genético
best_route, best_distance = genetic_algorithm(cities, distances)

# Exibir os resultados
route_names = [cities[i] for i in best_route]
print(f"Melhor rota: {' -> '.join(route_names)}")
print(f"Distância total: {best_distance} km")
