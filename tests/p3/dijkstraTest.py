#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.constants import test_tab

from package3.dijkstra import Dijkstra


dijkstra = Dijkstra(test_tab, 2)
dijkstra.solve()
dijkstra.print_result()