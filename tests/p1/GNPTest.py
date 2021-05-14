#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package1.gnp import GNP
from package1.plot import GraphPloter

print(GNP(10, 0.5).get_raw().sum())

GraphPloter(GNP(10, 0.5).graph).draw()