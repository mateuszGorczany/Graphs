import numpy as np

from utilities.GraphValidator import GraphValidator

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
    self.probability = probability
    self.__graph = np.zeros((n_verticies, n_verticies))

    self.__generate()
    GraphValidator.check_adjacency_matrix(self.__graph)

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

  # fixed - Klasa GNP generuje nieprawidłową macierz sąsiedztwa --- na diagonali 
  # może występować wartość 2 ; ma również publiczną metodę, która pozwala 
  # naruszyć symetrię macierzy ; Funkcja rysująca również nie wychwytuje ani 
  # uszkodzonej diagonali ani asymetrii i rysuje krawędzie tylko według relacji 
  # kolumna -> wiersz
  def __generate(self) -> None:
    """
    Generates adjacency matrix of a graph
    """
    for i in range(self.n_verticies):
      for j in range(i+1, self.n_verticies):
        if self.__is_edge():
          self.__graph[i,j] = 1
          self.__graph[j,i] = 1