import heapq
from graph import Graph


def dijkstra(graph: Graph, start_node: int) -> tuple[dict[int, int], dict[int, int]]:
    """
    Calcule les plus courts chemins depuis un nœud de départ vers tous les autres.
    Utilise l'algorithme de Dijkstra.

    return:
        - Un dictionnaire des distances les plus courtes.
        - Un dictionnaire des prédécesseurs pour reconstruire les chemins.
    """
    distances = {node: float('inf') for node in range(len(graph.vertices))}
    predecesseurs = {node: None for node in range(len(graph.vertices))}
    distances[start_node] = 0

    pq = [(0, start_node)]  # (distance, noeud)

    while pq:
        dist_actuelle, noeud_actuel = heapq.heappop(pq)

        if dist_actuelle > distances[noeud_actuel]:
            continue

        for voisin, poids, _ in graph.adjacency_list[noeud_actuel]:
            distance = dist_actuelle + poids
            if distance < distances[voisin]:
                distances[voisin] = distance
                predecesseurs[voisin] = noeud_actuel
                heapq.heappush(pq, (distance, voisin))

    return distances, predecesseurs