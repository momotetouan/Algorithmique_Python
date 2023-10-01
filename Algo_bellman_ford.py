def bellman_ford(graph, start):
    # Initialisation des distances à l'infini sauf pour le nœud de départ
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Relâchez les arêtes |V| - 1 fois, où |V| est le nombre de nœuds
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Vérification des cycles de poids négatif
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise Exception("Le graphe contient un cycle de poids négatif")
    
    return distances
