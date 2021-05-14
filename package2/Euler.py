import random
import numpy as np
from collections import deque

from package2.randomizer import Creator
from package2.bridges import find_bridges_DFS

class Euler():

  def __init__(self):
    # super().__init__(graphic_sequence)
    self.adjacency_matrix = None
    self.euler_path = None

  @property
  def adjacency_matrix_np(self):
    return np.array(self.adjacency_matrix)

  @staticmethod
  def generate_euler_graphic_sequence(n):
    graphic_sequence = []
    while len(graphic_sequence) < n:
      vertex_degree = random.randint(2, n-1)
      if vertex_degree % 2 == 0:
        graphic_sequence.append(vertex_degree)

    return graphic_sequence
  
  def generate_Euler_graph(self, n, max_iter=30):
    graph = None 
    counter = 0
    while graph is None:
      if counter > max_iter:
        raise Exception("Couldn't make graph with this kind of sequence")

      graph = Creator(Euler.generate_euler_graphic_sequence(n)).make_graph()
       
      if graph:
        self.adjacency_matrix = graph.adjacency_matrix
        return graph
      counter += 1

  def set_graph(self, adjacency_matrix):
    self.adjacency_matrix = adjacency_matrix

  def find_euler(self, start_vertex):
    if self.adjacency_matrix is None:
      raise Exception("Garph is not set.")

    self.euler_path = deque()
    vertex = start_vertex

    vertex_number = len(self.adjacency_matrix)
    while True:
      self.euler_path.append(vertex)
      first_neighbor = -1
      for i, value in enumerate(self.adjacency_matrix[vertex]):
        if value !=0:
          first_neighbor = i

      if first_neighbor == -1:
        return True 


      D = np.zeros([vertex_number]).tolist()
      
      find_bridges_DFS(self.adjacency_matrix, vertex, -1, 1 , D )

      edge = 0
      try:
        edge = self.adjacency_matrix[vertex].index(1, first_neighbor) 
      except ValueError:
        try:
          edge = self.adjacency_matrix[vertex].index(2, first_neighbor)
        except ValueError:
          print(first_neighbor)
          print(vertex)
          print(self.adjacency_matrix)
          
      self.adjacency_matrix[vertex][edge] =  self.adjacency_matrix[edge][vertex] = 0
      vertex = edge
    
    return True
