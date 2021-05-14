#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package2.Euler import Euler



#naprawic !


# test_matrix_with_euler = [
#   [0,1,1,0,0],
#   [1,0,1,1,1],
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,1,0,1,0]
# ]
# test_matrix_without_euler = [
#   [0,1,1,0,0],
#   [1,0,1,1,0],
#   [1,1,0,0,0],
#   [0,1,0,0,1],
#   [0,0,0,1,0]
# ]

# euler = Euler()

# S = euler.find_euler(0,test_matrix_with_euler)
# print(S)