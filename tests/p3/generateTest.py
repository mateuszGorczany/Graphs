#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.GraphDrawer import GraphDrawer

from package3.generate import generate_random_graph

drawer = GraphDrawer()
graph = generate_random_graph()

drawer.configure_from_adjacency_matrix(graph.get_raw(), isWeighted=True,a=1,b=10)
drawer.draw()