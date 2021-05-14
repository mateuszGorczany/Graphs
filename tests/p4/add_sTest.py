#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package4.digraphGNP import GNP
from utilities.GraphDrawer import GraphDrawer

G = GNP(5, 0.8)
G.randomize_distance(1,10)
G.add_s()

GraphDrawer().configure_from_adjacency_matrix(G.graph, isWeighted=True, weights=G.weights).draw()

