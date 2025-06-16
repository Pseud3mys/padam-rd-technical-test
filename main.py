from input import parse_cmd_line, parse_file
from graph import Graph
from example_solution import example_solution
from postierChinois import test
from utils import *


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
    #dist = floyd_warshall(graph)
    #print(dist)

    """print("Length of path found:", len(path) + 1)
    print("Value of path found:", sum(edge[2] for edge in path))"""

    if plot_graph:
        graph.plot()
        #graph.display_path(path=path)


if __name__ == "__main__":
    main()
