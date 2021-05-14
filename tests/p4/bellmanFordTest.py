#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.preety_print import preety_print
from utilities.GraphDrawer import GraphDrawer

from package4.digraphGNP import GNP
from package4.bellmanFord import BellmanFord

gnp = GNP(10, 0.3)
# preety_print(gnp.graph)
# print()
# print(kosaraju(gnp.graph))


W = gnp.randomize_distance(-20,100)

BellmanFord(gnp.graph,W,0).print_result()

GraphDrawer().configure_from_adjacency_matrix(gnp.graph, isWeighted=True, weights=W).draw()