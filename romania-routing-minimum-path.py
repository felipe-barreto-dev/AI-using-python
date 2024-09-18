import heapq

# Define o grafo das cidades da Romênia e as distâncias entre elas
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

# Função para encontrar o caminho mínimo usando o Algoritmo de Dijkstra
def dijkstra(graph, start, end):
    # Fila de prioridade para armazenar as distâncias
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    
    # Dicionário para armazenar as menores distâncias de cada cidade
    distances = {city: float('infinity') for city in graph}
    distances[start] = 0
    
    # Dicionário para armazenar o caminho anterior de cada cidade
    path = {city: None for city in graph}
    
    while priority_queue:
        current_dist, current_city = heapq.heappop(priority_queue)
        
        # Se chegamos no destino, paramos
        if current_city == end:
            break
        
        # Explorar as cidades vizinhas
        for neighbor, distance in graph[current_city].items():
            new_dist = current_dist + distance
            # Atualiza se encontrarmos um caminho mais curto
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                path[neighbor] = current_city
                heapq.heappush(priority_queue, (new_dist, neighbor))
    
    # Reconstruir o caminho mínimo
    final_path = []
    city = end
    while city is not None:
        final_path.append(city)
        city = path[city]
    
    final_path.reverse()
    return final_path, distances[end]

# Exemplo de uso: encontrar o caminho mínimo entre Arad e Bucharest
start = 'Arad'
end = 'Bucharest'
shortest_path, total_distance = dijkstra(romania_graph, start, end)

# Exibir o caminho e a distância total
print(f"Caminho mínimo de {start} para {end}: {' -> '.join(shortest_path)}")
print(f"Distância total: {total_distance} km")
