#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.preety_print import preety_print

from package4.digraphGNP import GNP

gnp = GNP(10, 0.3)
# preety_print(gnp.graph)
# print()
# print(kosaraju(gnp.graph))


W = gnp.randomize_distance(-20,100)

preety_print(W)
