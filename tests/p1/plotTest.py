#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package1.plot import GraphPloter
from utilities.generateTestMatrix import generateTestMatrix

ploter =  GraphPloter(generateTestMatrix(5)).draw()