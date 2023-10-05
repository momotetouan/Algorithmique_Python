import heapq

def prim(graph):
    # Sélectionnez un nœud de départ arbitraire (vous pouvez choisir n'importe quel nœud)
    start_node = list(graph.keys())[0]
    
    # Initialisez les structures de données nécessaires
    visited = set()
    min_spanning_tree = []
    min_heap = [(0, start_node)]

    while min_heap:
        # Sélectionnez le nœud avec le poids minimum
        weight, current_node = heapq.heappop(min_heap)
        
        # Si le nœud a déjà été visité, passez au suivant
        if current_node in visited:
            continue
        
        # Marquez le nœud comme visité
        visited.add(current_node)
        
        # Ajoutez le nœud au minimum spanning tree
        if weight > 0:
            min_spanning_tree.append((current_node, weight))
        
        # Parcourez les voisins non visités du nœud actuel
        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return min_spanning_tree

# Exemple d'utilisation
if __name__ == "__main__":
    # Format du graphe : {noeud1: [(voisin1, poids1), (voisin2, poids2)], ...}
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 4), ('D', 5)],
        'C': [('A', 3), ('B', 4), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    minimum_spanning_tree = prim(graph)
    print("Arbre couvrant de poids minimal:")
    for edge in minimum_spanning_tree:
        print(edge)
