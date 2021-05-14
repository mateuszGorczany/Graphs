import networkx as nx
import random
import matplotlib.pyplot as plt
from copy import copy

from utilities.GraphValidator import GraphValidator
from package2.sequence import SequenceChecker

class GraphDrawer:
    def __init__(self):
        self.G = nx.Graph()
        self.comps = []
        self.colors = []

    def configure_from_sequence(self, seq):
        self.G.add_nodes_from(seq)
        n = len(seq)
        seq_cpy: list = copy(seq)

        for node, edge_count in enumerate(seq_cpy):
            locally_used = []
            for _ in range(edge_count):
                if edge_count == 0:
                    break
                other_node = self.get_first_max(seq_cpy, node, locally_used)
                locally_used.append(other_node)
                
                self.G.add_edge(node,other_node)
                seq_cpy[node] -= 1
                seq_cpy[other_node] -= 1

    def get_first_max(self, arr, current, used):
        maxx = 0
        pos = 0
        for i, val in enumerate(arr):
            if maxx < val and i != current and i not in used:
                maxx = val
                pos = i
        return pos

    def configure_from_adjacency_matrix(self, matrix, comps=None, isWeighted=False, weights=None, a=0, b=0):
        if not GraphValidator.is_adjacency_matrix_symetric(matrix):
            self.G = nx.DiGraph()
        else:
            self.G = nx.Graph()

        if comps:
            self.comps = comps
            for i in range(len(comps)):
                self.colors.append((random.random(), random.random(), random.random()))
                
        for i in range(len(matrix)):
            self.G.add_node(i)
            
        for i in range(1, len(matrix)):
            for j in range(0, i):
                if matrix[i][j] == 1:
                    if isWeighted and not weights:
                        self.G.add_weighted_edges_from([(i, j, random.randint(a,b))])
                    elif isWeighted and weights:
                        if isinstance(self.G, nx.DiGraph):
                            self.G.add_weighted_edges_from([(i,j, weights[i][j])])
                            if(matrix[j][i] == 1):
                                self.G.add_weighted_edges_from([(j,i, weights[i][j])])
                        pass
                    else:
                        self.G.add_edge(i, j)
        return self
        
    def draw(self):
        try:
            nx.draw(self.G, with_labels=True, pos=nx.planar_layout(self.G))
            nx.draw_networkx_edge_labels(self.G, pos=nx.planar_layout(self.G), edge_labels=nx.get_edge_attributes(self.G, 'weight'))
        except:
            nx.draw(self.G, with_labels=True, pos=nx.spring_layout(self.G))
            # nx.draw_networkx_edge_labels(self.G, pos=nx.spring_layout(self.G), edge_labels=nx.get_edge_attributes(self.G, 'weight'))
        plt.show()