import numpy as np
import math
import random
from typing import List

from utilities.GraphValidator import GraphValidator

class GNL:
  """
  Creates random graph on constructor input 
  """
  def __init__(self, n_verticies: int, n_edges: int):
    """
    Parameters
    ----------
      n_verticies : int 
        Number of verticies
      n_edges : int 
        Number of edges
    """
    if n_verticies < 1:
      raise RuntimeError("Wrong number of verticies")
    
    if not (0 <= n_edges <= n_verticies*(n_verticies - 1)/2 ):
      raise RuntimeError("Wrong number of edges")

    self.n_verticies = n_verticies
    self.n_edges = n_edges
    self.__graph = np.zeros((n_verticies, n_verticies))
    self.__edges_to_pick = [x for x in range(math.ceil(self.n_verticies * self.n_verticies))]

    self.__generate()
  
  @property
  def graph(self) -> List[List[int]]:
    """
    Returns
    -------
      Adjacency matrix
    """
    return self.__graph.astype("int32").tolist()

  def get_raw(self) -> np.ndarray:
    """
    Returns
    -------
      Adjacency matrix
    """
    return self.__graph
  
  def __generate(self) -> None:
    """
    Generates adjacency matrix of a graph

    Throws
    ------
      Exception when generated graph is not valid
    """
    counter = 0
    while counter < self.n_edges:
      random_index = random.randint(0, len(self.__edges_to_pick) - 1)
      value = self.__edges_to_pick[random_index]
      del self.__edges_to_pick[random_index]

      i = value % self.n_verticies
      j = math.floor(value / self.n_verticies)
    
      if self.__graph[i,j] == 1 or i == j:
        continue
      else:
        self.__graph[i,j] = 1
        self.__graph[j,i] = 1
        counter += 1
    
    if GraphValidator.count_n_edges(self.__graph) != self.n_edges or not GraphValidator.is_adjacency_matrix(self.__graph):
      raise Exception("Method failure")