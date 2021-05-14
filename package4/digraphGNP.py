import random
import numpy as np

from utilities.print_matrix import print_matrix

class GNP:
  """
  Creates random graph based on constructor input
  """
  def __init__(self, n_verticies: int, probability) -> None:
    """
    Parameters
    ----------
      n_verticies : int 
        Number of verticies
      probability : float 
        Probability of connection between nodes
    """
    if not (0 <= probability <= 1):
      raise RuntimeError("Wrong value of p")
    if n_verticies < 1:
      raise RuntimeError("Wrong value of n")

    self.n_verticies = n_verticies
    self.weights = [0 for _ in range(self.n_verticies)]
    self.probability = probability
    self.__graph = np.zeros((n_verticies, n_verticies))

    self.__generate()

  def add_s(self):
    self.randomize_distance(1,10)
    for i,row in enumerate(self.weights):
      self.weights[i].append(0)
    
    self.weights.append([0 for i in range(self.n_verticies)])
 
    print_matrix(self.__graph)
    self.__graph.resize(self.n_verticies+1, self.n_verticies+1)

    for i in range(self.n_verticies+1):
      self.__graph[-1][i] = 1
      self.__graph[i][-1] = 0
      self.__graph[i][i] = 0

    print_matrix(self.graph)
    self.n_verticies += 1


  def __is_edge(self) -> bool:
    """
    Checks whether given number is an edge
    """
    return np.random.random() < self.probability

  @property
  def graph(self):
    """Converts numpy array to list of lists"""
    return self.__graph.astype("int32").tolist()

  def get_raw(self) -> np.ndarray:
    """"Returns numpy array"""
    return self.__graph

  def __generate(self) -> None:
    """
    Generates adjacency matrix of a graph
    """
    for i in range(self.n_verticies):
      for j in range(self.n_verticies):
        if i != j and self.__is_edge():
          self.__graph[i,j] = 1

  def randomize_distance(self, start,end):
    self.weights = [[random.randint(start, end)for i in range(len(self.__graph))] for j in range(len(self.__graph))]
    return self.weights