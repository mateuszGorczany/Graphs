#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from utilities.preety_print import preety_print
from utilities.constants import test_tab

from utilities.distance import create_distance_matrix



distance_matrix = create_distance_matrix(test_tab)
preety_print(distance_matrix)