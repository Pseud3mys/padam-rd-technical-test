from input import parse_cmd_line, parse_file
from graph import Graph
from example_solution import example_solution
from postierChinois import test


def main():
    #in_file, plot_graph = parse_cmd_line()
    plot_graph = False
    in_file = "instances/paris_map.txt"  # Default input file, can be changed as needed
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")
    graph = Graph(vertices, edges)

    path = example_solution(graph)
    test(graph)

    print("Length of path found:", len(path) + 1)
    print("Value of path found:", sum(edge[2] for edge in path))

    if plot_graph:
        graph.plot()
        graph.display_path(path=path)


if __name__ == "__main__":
    main()
