from graph import Graph


def test(graph: Graph):
    even_edge = []
    uneven_edge = []
    # parcours les sommets et garde en mémoire tous les sommets de degree pair/impaire
    for sommet in range(len(graph.vertices)):
        degree_sommet = sum(1 for value in graph.adjacency_matrix[sommet] if value != 0)
        if degree_sommet % 2 == 0:
            even_edge.append(sommet)
        else:
            uneven_edge.append(sommet)
    print("even_edge:", even_edge)
    print("uneven_edge:", uneven_edge)  # doit être un nombre pair.
    if len(uneven_edge) == 0:
        print("Le graphe est déjà eulerien.")
    print("nombre total de sommets:", len(graph.vertices))


