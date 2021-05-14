#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package2.composition import components
from package2.composition import find_max_subgraph

from utilities.GraphDrawer import GraphDrawer
from utilities.GenerateGraph import GenerateGraph

G = GenerateGraph(20, 0.09)

drawer = GraphDrawer()

graph_as_adjacency_matrix = G.get_raw()

comps = components(graph_as_adjacency_matrix)
print(comps)
print(find_max_subgraph(comps))

drawer.configure_from_adjacency_matrix(graph_as_adjacency_matrix, comps)
drawer.draw()