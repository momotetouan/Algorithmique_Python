import heapq

def dijkstra(graph, start):
    # Initialisation des distances à l'infini sauf pour le nœud de départ
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Création d'une file de priorité pour explorer les nœuds avec les distances les plus faibles en premier
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Obtenez le nœud avec la distance minimale
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Si la distance actuelle est supérieure à la distance enregistrée, ignorez ce nœud
        if current_distance > distances[current_node]:
            continue
        
        # Parcourez les voisins du nœud actuel
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Si une distance plus courte est trouvée, mettez à jour la distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
