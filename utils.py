import heapq  # structure plus opti que les 'list' python pour cette application (ajouter/enlever un element au début).

#import graph
from graph import *


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
    return chemin[::-1]  # le chemin est donnée à l'envers par les predecesseurs (meme si ici c'est un graph non
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

def vertices_path_to_edges(graph: Graph, vertices_path: list[int]) -> list[Edge]:
    edges = [
        (
            vertices_path[i],
            vertices_path[i + 1],
            graph.adjacency_matrix[vertices_path[i]][vertices_path[i + 1]],
            graph.vertices[vertices_path[i]],
            graph.vertices[vertices_path[i + 1]],
        )
        for i in range(len(vertices_path) - 1)
    ]
    return edges

def hierholzer(graph_eulérien: Graph, start_node: int = 0) -> list[Edge]:
    """
    Trouve un circuit eulérien dans un graphe où tous les sommets ont un degré pair,
    en utilisant l'algorithme de Hierholzer.

    Return
    list[int]
        La séquence de sommets formant le circuit eulérien.
    """
    # On crée une copie de la liste d'adjacence pour pouvoir la modifier.
    adj = {u: list(neighbors) for u, neighbors in graph_eulérien.adjacency_list.items()}

    circuit = []
    stack = [start_node]

    while stack:
        current_vertex = stack[-1]

        # S'il y a des arêtes non visitées depuis le sommet actuel
        if adj[current_vertex]:
            # On choisit une arête
            neighbor, _, edge_id = adj[current_vertex].pop()

            # On supprime l'arête inverse pour ne pas la reparcourir
            # C'est une étape cruciale dans un graphe non-orienté
            for i, (v_n, _, e_id_n) in enumerate(adj[neighbor]):
                if v_n == current_vertex and e_id_n == edge_id:
                    adj[neighbor].pop(i)
                    break

            # On avance au sommet suivant
            stack.append(neighbor)

        # Si le sommet actuel n'a plus d'arête sortante non visitée
        else:
            # On a complété un cycle, on revient en arrière.
            # On ajoute le sommet au début de notre circuit final.
            circuit.append(stack.pop())

    # Le circuit est construit à l'envers, on le retourne
    vertices_path = circuit[::-1]
    return vertices_path_to_edges(graph_eulérien, vertices_path)

def euclidean_distance(graph: Graph, id1: int, id2: int) -> float:
    """
    Distance à vol d'oiseau entre deux sommets du graphe.
    Pour faire des heuristiques.
    """
    x1, y1 = graph.vertices[id1]
    x2, y2 = graph.vertices[id2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def floyd_warshall(graph: Graph, sommets_a_relier: [int]) -> list[list[float]]:
    """
    Calcule les plus courts chemins entre toutes les paires de sommets du graphe.
    Utilise l'algorithme de Floyd-Warshall.

    Utilise une liste d'adjacence.

    Cette fonction à été adaptée pour ne calculer que les distances entre 'sommets_a_relier'.
    De plus il y a une heuristique pour se limiter à un certain rayon.

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
        if k%50 == 0:  # Afficher l'avancement tous les 50 sommets.
            print(f"Processing intermediate vertex {k+1}/{num_vertices}...")
        for i in sommets_a_relier:
            if euclidean_distance(graph, i, k) > 0.005:  # Heurisitque pour Paris.
                # problème de ce truc: si j est plus loin que ca de i alors il n'y aura pas de paire créer...
                # Il faut esperer que chaque sommet impaire à un autre sommet impaire dans son voisinage...
                continue
            for j in sommets_a_relier:
                # Si le chemin de i à j via k est plus court, on met à jour la distance.
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist