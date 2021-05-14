#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.constants import prim_test
from utilities.preety_print import preety_print

from package3.prim import Prim


p = Prim(prim_test)
p.find_tree()
p.draw_graph()

p.draw_tree()

preety_print(p.tree)