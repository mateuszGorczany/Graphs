#Make packages visible for this file
import sys
import os
sys.path.append(os.path.curdir)
#Testing code below

from package1.conversion import GraphRepresentationConverter
from utilities.print_matrix import print_matrix

test_adjacency_matrix =[
  [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0], 
  [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
  [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0], 
  [0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0] 
]

test_adjacency_list = [[1, 4, 5], [0, 2, 5], [1, 3, 4, 11], [2, 7, 8, 10], [0, 2, 6, 8], [0, 1, 6], [4, 5, 7], [3, 6, 8, 11], [3, 4, 7, 9], [8], [3], [2, 7]]

test_incidence_matrix = [
  [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
  [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0], 
  [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], 
  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

result_adjacency_list = GraphRepresentationConverter.adjacency_matrix_to_adjacency_list(test_adjacency_matrix)
# print_matrix(result_adjacency_list)
if(result_adjacency_list == test_adjacency_list):
  print("Good output, test passed")


result_incidence_matrix = GraphRepresentationConverter.adjacency_list_to_incidence_matrix(test_adjacency_list)
# print_matrix(result_incidence_matrix)
if(result_incidence_matrix == test_incidence_matrix):
  print("Good output, test passed")

result_adjacency_matrix = GraphRepresentationConverter.adjacency_list_to_adjacency_matrix(test_adjacency_list)
# print_matrix(result_adjacency_matrix)
if(result_adjacency_matrix == test_adjacency_matrix):
  print("Good output, test passed")

result_adjacency_list = GraphRepresentationConverter.incidence_matrix_to_adjacency_list(test_incidence_matrix)
# print_matrix(result_adjacency_list)
if(result_adjacency_list == test_adjacency_list):
  print("Good output, test passed")

result_adjacency_matrix = GraphRepresentationConverter.incidence_matrix_to_adjacency_matrix(test_incidence_matrix)
# print_matrix(result_adjacency_matrix)
if(result_adjacency_matrix == test_adjacency_matrix):
  print("Good output, test passed")

result_incidence_matrix = GraphRepresentationConverter.adjacency_matrix_to_incidence_matrix(test_adjacency_matrix)
# print_matrix(result_incidence_matrix)
if(result_incidence_matrix == test_incidence_matrix):
  print("Good output, test passed")