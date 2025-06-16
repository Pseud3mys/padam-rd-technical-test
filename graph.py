from __future__ import annotations

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np

Coordinates = tuple[float, float]
Edge = tuple[int, int, int, Coordinates, Coordinates]


class Graph:
    def __init__(
        self,
        vertices: list[Coordinates],
        edges: list[Edge],
    ):
        """Basic constructor of a `Graph` instance.

        Parameters
        ----------
        vertices : list[Coordinates]
            List of vertices coordinates.

        edges : list[Edge]
            List of edges as tuple (id 1, id 2, weight, coordinates 1, coordinates 2).
        """
        self.vertices = vertices
        self.edges = edges
        self.adjacency_matrix = self._creer_matrice()
        self.adjacency_list = self._creer_liste_adjacence()

    def plot(self):
        """
        Plot the graph.
        """
        weights = list(set(edge[2] for edge in self.edges))
        colors = plt.cm.get_cmap("viridis", len(weights))
        _, ax = plt.subplots()
        for i, weight in enumerate(weights):
            lines = [
                [edge[-2][::-1], edge[-1][::-1]]
                for edge in self.edges
                if edge[2] == weight
            ]
            ax.add_collection(
                LineCollection(
                    lines, colors=colors(i), alpha=0.7, label=f"weight {weight}"
                )
            )
        ax.plot()
        ax.legend()
        plt.title(f"#E={len(self.edges)}, #V={len(self.vertices)}")
        plt.show()

    def _creer_matrice(self):
        """Crée la matrice d'adjacence à partir des arêtes."""
        n = len(self.vertices)
        matrix = [[0] * n for _ in range(n)]
        for edge in self.edges:
            i, j, weight = edge[0], edge[1], edge[2]
            matrix[i][j] = weight
            matrix[j][i] = weight
        return np.array(matrix)

    def _creer_liste_adjacence(self):
        """Crée une liste d'adjacence à partir des arêtes."""
        n = len(self.vertices)
        adj_list = {i: [] for i in range(n)}
        for i, edge in enumerate(self.edges):
            u, v, weight, _, _ = edge
            adj_list[u].append((v, weight, i))
            adj_list[v].append((u, weight, i))
        return adj_list

    @classmethod
    def display_path(cls, *, path: list[Edge]):
        return cls.display_paths(paths=[path])

    @staticmethod
    def display_paths(*, paths: list[list[Edge]]):
        colors = plt.cm.get_cmap("viridis", len(paths))
        figure = plt.figure()
        ax = figure.add_subplot()
        for path_index, path in enumerate(paths):
            for edge_index, edge in enumerate(path):
                ax.annotate(
                    str(edge_index),
                    xytext=edge[3],
                    xy=edge[4],
                    arrowprops=dict(arrowstyle="->", color=colors(path_index)),
                )
        plt.show()
