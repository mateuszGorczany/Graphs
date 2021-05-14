import numpy as np
import math
from typing import List

class GraphValidator:
  """
  Validation methods for undirected graph
  """
  @staticmethod
  def count_n_edges(adjacency_matrix: List[List[int]]) -> int:
    """
    Counts number of edges in :adjacency_matrix

    Returns
    -------
      int
        number of edges
    """
    adjacency_matrix_np = np.array(adjacency_matrix)
    return math.floor(np.count_nonzero(adjacency_matrix_np)/2)

  @staticmethod
  def is_adjacency_matrix_quadratic(adjacency_matrix: List[List[int]]) -> bool:
    """
    Checks whether :adjacency_matrix is quadratic

    Returns
    -------
    bool
      Returns true when matrix is quadratic
    """
    adjacency_matrix_np = np.array(adjacency_matrix)
    return adjacency_matrix_np.shape[0] == adjacency_matrix_np.shape[1]


  @staticmethod
  def is_adjacency_matrix_diagonal_empty(adjacency_matrix: List[List[int]]) -> bool:
    """
    Checks whether :adjacency_matrix diagonal is filled with zeros

    Returns
    -------
    bool
      Returns true when matrix diagonal is filled with zeros
    """
    return np.trace(adjacency_matrix) == 0
  
  @staticmethod
  def is_adjacency_matrix_symetric(adjacency_matrix: List[List[int]]) -> bool:
    """
    Checks whether :adjacency_matrix is symetric

    Returns
    -------
    bool
      True when matrix is symetric
    """
    adjacency_matrix_np = np.array(adjacency_matrix)

    return np.abs(adjacency_matrix_np - adjacency_matrix_np.T).sum() == 0

  @staticmethod
  def is_adjacency_list(adjacency_list: List[int]) -> bool:
    """
    Check whether :adjacency_list represents adjacency list

    Returns
    -------
    bool
      True when :adjacency_list is adjacency list
    """
    for current_node,sublist in enumerate(adjacency_list):
      for other_node in sublist:
        if current_node not in adjacency_list[other_node]:
          return False
    return True

  @staticmethod
  def is_incidence_matrix(incidence_matrix: List[List[int]]) -> bool:
    """ 
    Checks whether :incidence_matrix is incidence matrix

    Returns
    -------
    bool
      True when :incidence_matrix is incidence matrix
    """
    incidence_matrix_np = np.array(incidence_matrix)
    return np.all(incidence_matrix_np.sum(axis=0) == 2)

  @staticmethod
  def is_adjacency_matrix(adjacency_matrix: List[List[int]]) -> bool:
    """
    Checks whether :adjacency_matrix is adjacency matrix
    
    Returns
    -------
    bool
      Returns true when :adjacency_matrix represents graph's adjacency_matrix
    """
    return GraphValidator.is_adjacency_matrix_quadratic(adjacency_matrix) and\
           GraphValidator.is_adjacency_matrix_diagonal_empty(adjacency_matrix) and\
           GraphValidator.is_adjacency_matrix_symetric(adjacency_matrix)
  
  @staticmethod
  def check_adjacency_matrix(adjacency_matrix: List[List[int]]) -> None:
    """
    Checks whether :adjacency_matrix represents adjacency matrix 
 
    Throws
    ------
      Exception when :adjacency_matrix does not represent adjacency matrix of undirected graph 
    """
    if not GraphValidator.is_adjacency_matrix(adjacency_matrix):
      raise Exception("Wrong input")

  @staticmethod
  def check_incidence_matrix(incidence_matrix: List[List[int]]) -> None:
    """
    Checks whether :incidence_matrix is incidence matrix
    
    Throws
    ------
      Exception when :incidence_matrix does not represent incidence matrix of undirected graph 
    """
    if not GraphValidator.is_incidence_matrix(incidence_matrix):
      raise Exception("Wrong input")

  @staticmethod
  def check_adjacency_list(adjacency_list: List[int]) -> None:
    """
    Checks whether :adjacency_list is adjacency list
    
    Throws
    ------
      Exception when :adjacency_list does not represent adjacency list of undirected graph 
    """
    if not GraphValidator.is_adjacency_list(adjacency_list):
      raise Exception("Wrong input")