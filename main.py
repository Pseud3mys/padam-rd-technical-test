from input import parse_cmd_line, parse_file
from graph import Graph
from example_solution import example_solution
from postierChinois import test
from utils import *

""" ---------------------------
Tout le code utile est dans utils.py et j'ai rajouter qlq fonction à graph.py
Et le code ne se run plus via le terminal mais via un main.py
--------------------------- """

def main():
    #in_file, plot_graph = parse_cmd_line()
    plot_graph = True
    in_file = "instances/paris_map.txt"  # Default input file, can be changed as needed
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")
    graph = Graph(vertices, edges)
    Sommets_impairs = trouver_sommets_impairs(graph)
    print("#Sommets de degré impair:", len(Sommets_impairs))

    print("Fin initialisation du graphe.")
    """ce temps ne compte pas vraiment dans l'algo
    en effet, le graph ne change pas entre deux trajets à trouver"""

    #path = example_solution(graph)
    #test(graph)
    #dist = floyd_warshall(graph, sommets_a_relier=Sommets_impairs)
    #print(dist)
    path = hierholzer(graph)
    print("hierholzer finit")

    sommets_a_apparier = list(Sommets_impairs)
    paires_trouvees = []
    poids_additionnel = 0

    while sommets_a_apparier:
        #print(poids_additionnel, len(sommets_a_apparier), "sommets à apparier restants")
        poids_min = float('inf')
        u_final, v_final = -1, -1

        # Itère sur toutes les combinaisons de sommets restants
        for i in range(len(sommets_a_apparier)):
            for j in range(i + 1, len(sommets_a_apparier)):
                u = sommets_a_apparier[i]
                v = sommets_a_apparier[j]

                dist = euclidean_distance(graph, u, v)

                if dist < poids_min:
                    poids_min = dist
                    u_final, v_final = u, v

                if poids_min <= 0.005:  # Seuil pour arrêter la recherche (c'est ajusté pour Paris en gros.)
                    break

        # Ajoute la meilleure paire trouvée à la solution
        paires_trouvees.append((u_final, v_final))
        poids_additionnel += poids_min

        # Retire les sommets de la liste pour la prochaine itération
        sommets_a_apparier.remove(u_final)
        sommets_a_apparier.remove(v_final)

    print("Paires formées (méthode gloutonne) :", paires_trouvees)
    print("Poids total additionnel :", poids_additionnel)


    print("Length of path found:", len(path) + 1)
    print("Value of path found:", sum(edge[2] for edge in path))

    if plot_graph:
        # plot the odd degree vertices
        graph.plot_vertexes(Sommets_impairs, color='red', size=1)
        # plot paires_trouvees
        graph.plot_edges(paires_trouvees, color='green', size=1)
        plt.plot()

        graph.plot()
        graph.display_path(path=path)


if __name__ == "__main__":
    main()
