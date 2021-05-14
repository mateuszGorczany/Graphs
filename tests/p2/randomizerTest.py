#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package2.randomizer import Creator
from utilities.print_matrix import print_matrix

vg = [4,2,2,3,2,1,4,2,2,2,2]

cr = Creator(vg).make_graph()
cr.draw()

cr.randomize(5).draw()

graph2 = Creator([4,2, 6, 2, 6, 2, 4, 2]).make_graph()
graph2.draw()

if cr.adjacency_matrix_np.sum(axis=1).tolist() == vg:
    print("test passed")

print_matrix(graph2.adjacency_matrix_np)

graph2.draw()

print(graph2.adjacency_matrix_np.sum(axis=1))