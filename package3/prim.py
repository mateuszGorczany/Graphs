import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Prim:

    def __init__(self, adjacency_matrix):
        """
        adjacancy_matrix: list of lists
        """
        self.__adjacency_matrix = np.array(adjacency_matrix)
        self.__tree = np.zeros_like(adjacency_matrix)
        self.n_verticies = self.__adjacency_matrix.shape[0]

    @property
    def tree(self):
        return self.__tree.tolist()

    @property
    def adjacency_matrix(self):
        return self.__adjacency_matrix.tolist()

    def find_tree(self):
        selected = np.zeros(self.n_verticies, dtype=bool)
        selected[0] = True
        current_edge = 0

        while current_edge < self.n_verticies - 1:
            lightest_edge = np.inf
            x, y = 0, 0

            for is_selected, i in zip(selected, range(self.n_verticies)):
                if is_selected:
                    for j in range(self.n_verticies):
                        is_connected = self.__adjacency_matrix[i][j] != 0
                        if not selected[j] and is_connected:
                            lightest_edge_is_no_longer_lightest = lightest_edge > self.adjacency_matrix[i][j]

                            if lightest_edge_is_no_longer_lightest:
                                lightest_edge = self.__adjacency_matrix[i][j]
                                x, y = i, j

            self.__tree[x,y] = self.__tree[y,x] = self.__adjacency_matrix[x,y]
            selected[y] = True
            current_edge += 1

        return self.tree

    def draw(self, adjacency_matrix):
        nx.draw_circular(nx.Graph(adjacency_matrix), with_labels=True)
        plt.show()
    
    def draw_tree(self):
        self.draw(self.__tree)

    def draw_graph(self):
        self.draw(self.__adjacency_matrix)