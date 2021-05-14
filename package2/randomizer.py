import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Creator:

  def __init__(self, graphic_sequence):
    self.graphic_sequence = graphic_sequence
    self.n_verticies = len(self.graphic_sequence)
    self.__adjacency_matrix = np.zeros((self.n_verticies, self.n_verticies), dtype=int)
    self.__sorted_graphic_sequence = self.graphic_sequence.copy()
    self.__sorted_graphic_sequence.sort(reverse=True)
    self.__new_idxs = (-np.array(self.graphic_sequence)).argsort().tolist()

    self.__where_ones = None
     

  @property
  def adjacency_matrix_np(self):
    return self.__adjacency_matrix

  @property
  def adjacency_matrix(self):
    return self.__adjacency_matrix.tolist()
    
  def make_graph(self):
    graphic_sequence = self.__sorted_graphic_sequence.copy()

    for index, connections_left in enumerate(graphic_sequence):
      new_connection_index = index + 1
      while connections_left > 0:
        if new_connection_index > len(graphic_sequence)-1:
            break

        if graphic_sequence[new_connection_index] > 0:
            self.__adjacency_matrix[index, new_connection_index] = 1
            self.__adjacency_matrix[new_connection_index, index] = 1

            graphic_sequence[new_connection_index] -= 1
            connections_left -= 1

        new_connection_index += 1
    
      graphic_sequence[index] = 0
    

    self.__permute_matrix(self.__new_idxs)
    if not self.__is_valid():
      return None
    
    self.__where_ones = np.vstack(np.where(self.__adjacency_matrix == 1)).T
    return self

  def __permute_matrix(self, indexes):
      m2 = self.__adjacency_matrix.copy()
      m2[indexes] = self.__adjacency_matrix  
      self.__adjacency_matrix[indexes] = m2.T
  
  def randomize(self, how_many):
    while how_many > 0:
      rand_pair1 = np.random.randint(0, self.__where_ones.shape[0])
      rand_pair2 = np.random.randint(0, self.__where_ones.shape[0])

      a, b = self.__where_ones[rand_pair1]
      c, d = self.__where_ones[rand_pair2]

      is_on_diagonal = a==d or c==b
      is_alerady_connected = [a,d] in self.__where_ones.tolist() or [c,b] in self.__where_ones.tolist()
      if is_on_diagonal or is_alerady_connected:
        continue

      self.__adjacency_matrix[a,b] = 0
      self.__adjacency_matrix[b,a] = 0
      self.__adjacency_matrix[a,d] = 1
      self.__adjacency_matrix[d,a] = 1

      self.__adjacency_matrix[c,d] = 0
      self.__adjacency_matrix[d,c] = 0
      self.__adjacency_matrix[c,b] = 1
      self.__adjacency_matrix[b,c] = 1

      self.__where_ones = np.vstack(np.where(self.__adjacency_matrix == 1)).T

      if not self.__is_valid():
        raise Exception(f"Wrong output, shuffles left: {how_many}")

      how_many -= 1
    
    return self

  def __is_valid(self):
    return self.__adjacency_matrix.sum(axis=1).tolist() == self.graphic_sequence

  def draw(self):
    fig = nx.draw_circular(nx.Graph(self.__adjacency_matrix), with_labels=True)
    plt.show()