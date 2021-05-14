#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.GraphValidator import GraphValidator

from package1.gnl import GNL
from package1.plot import GraphPloter

super_test = GNL(100, 4920).graph
GraphValidator.count_n_edges(super_test)
GraphPloter(super_test).draw()