#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.GraphDrawer import GraphDrawer


sequence = [4,2,4,3,2,4,3,2,2]
GraphDrawer().configure_from_sequence(sequence).draw()

try:
    sequence = [3,3,3]
    GraphDrawer().configure_from_sequence(sequence).draw()
except:
    print("exception thrown test passed")