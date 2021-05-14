#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.constants import test_tab

from package3.graphCenter import find_graph_center
from package3.graphCenter import find_minimax_graph_center

center, s = find_graph_center(test_tab)
print(f'Centrum  = {center} (suma dleglosci: {s})')

center, m = find_minimax_graph_center(test_tab)
print(f'Centrum minimax  = {center} (odleglosc od najdalszego: {m})')