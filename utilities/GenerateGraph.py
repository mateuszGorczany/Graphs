import numpy as np

class GenerateGraph:
  
  def __init__(self, n_verticies, probability):
    if not (0 <= probability and probability <= 1):
      raise RuntimeError("Wrong value of p")
    if n_verticies < 1 or not isinstance(n_verticies, int):
      raise RuntimeError("Wrong value of n")

    self.n_verticies = n_verticies
    self.probability = probability
    self.__graph = np.zeros((n_verticies, n_verticies))

    self.generate()
    self.__graph = self.__graph + self.__graph.T
  
  def __is_edge(self):
    return np.random.random() < self.probability

  @property
  def graph(self):
    return self.__graph.astype("int32").tolist()

  def get_raw(self):
    return self.__graph
  
  def generate(self):
    for i in range(self.n_verticies):
      for j in range(i):
        if self.__is_edge():
          self.__graph[i,j] = 1