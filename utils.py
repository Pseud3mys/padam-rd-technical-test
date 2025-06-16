import heapq  # structure plus opti que les 'list' python pour cette application (ajouter/enlever un element au début).
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

def reconstruire_chemin(predecesseurs: dict, depart: int, fin: int) -> list[int]:
    """Reconstruit le chemin le plus court entre deux nœuds. Fonctionne avec la sortie de Dijkstra."""
    chemin = []
    actuel = fin
    while actuel is not None:
        chemin.append(actuel)
        if actuel == depart:
            break
        actuel = predecesseurs[actuel]
    return chemin[::-1]  # le chemon est donnée à l'envers par les predecesseurs (meme si ici c'est un graph non
    # orienté).

def trouver_sommets_impairs(graph: Graph) -> list[int]:
    """
    Identifie tous les sommets de degré impair dans le graphe.
    """
    impairs = []
    for i in range(len(graph.vertices)):
        if len(graph.adjacency_list[i]) % 2 != 0:
            impairs.append(i)
    return impairs

def floyd_warshall(graph: Graph) -> list[list[float]]:
    """
    Calcule les plus courts chemins entre toutes les paires de sommets du graphe.
    Utilise l'algorithme de Floyd-Warshall.

    Cette fonction est adaptée aux graphes représentés par une liste d'adjacence,
    en construisant une matrice d'adjacence initiale.

    Returns:
        Une matrice de distances (liste de listes) où dist[i][j]
        représente la distance la plus courte du sommet i au sommet j.
    """
    num_vertices = len(graph.vertices)

    # Initialiser la matrice des distances avec l'infini.
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # La distance d'un sommet à lui-même est toujours 0.
    for i in range(num_vertices):
        dist[i][i] = 0

    # Remplir la matrice avec les poids des arêtes existantes.
    for u in range(num_vertices):
        for v, poids, _ in graph.adjacency_list[u]:
            dist[u][v] = poids

    # Algorithme de Floyd-Warshall.
    # On teste pour chaque paire (i, j) si passer par un sommet k est plus court.
    for k in range(num_vertices):
        print(f"Processing intermediate vertex {k+1}/{num_vertices}...")
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Si le chemin de i à j via k est plus court, on met à jour la distance.
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist