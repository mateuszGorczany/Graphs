from utilities.GraphValidator import GraphValidator
from typing import List

class GraphRepresentationConverter:
  @staticmethod
  def adjacency_matrix_to_adjacency_list(adjacency_matrix: List[List[int]]) -> List[int]:
    '''
    Converts adjacency matrix to adjacency list.

    Parameters
    ----------
        adjacency_matrix is list of lists that are equaly long and number of inner lists are equal to their length. Inner list consists of 1 and 0 representing connection

    Returns
    -------
        adjacency list is list of lists. Length of outer list is equal to number of vertices. Inner list is empty if there is no connection to this vertex
    '''
    GraphValidator.check_adjacency_matrix(adjacency_matrix)

    adjacency_list = []

    for row_index, row in enumerate(adjacency_matrix):
      adjacency_list.append([])
      for column_index, column in enumerate(row):
        if column == 1:
          adjacency_list[row_index].append(column_index)

    return adjacency_list

  @staticmethod
  def adjacency_list_to_adjacency_matrix(adjacency_list):
    ''' Parameters
    ----------
    adjacency_matrix : list[list[int]] or string
      
    formats:
      as string 
      1.  2 5 6
      2.  1 3 6
      3.  2 4 5 12
      4.  3 8 9 11
      5.  1 3 7 9
      6.  1 2 7
      7.  5 6 8
      8.  4 7 9 12
      9.  4 5 8 10
      10. 9
      11. 4
      12. 3 8
      
      as list of lists
      [[1, 4, 5],
      [0, 2, 5],
      [1, 3, 4, 11],
      [2, 7, 8, 10],
      [0, 2, 6, 8],
      [0, 1, 6],
      [4, 5, 7],
      [3, 6, 8, 11],
      [3, 4, 7, 9],
      [8],
      [3],
      [2, 7]]
      '''
    if isinstance(adjacency_list, str):
      adjacency_list = GraphRepresentationConverter.parse_adjacency_list(adjacency_list)
    
    GraphValidator.is_adjacency_list(adjacency_list)
    adjacency_matrix = []

    for row_index, row in enumerate(adjacency_list):
      adjacency_matrix.append([])
      for column in range(len(adjacency_list)):
        if(column in row):
          adjacency_matrix[row_index].append(1)
        else:
          adjacency_matrix[row_index].append(0)

    return adjacency_matrix

  @staticmethod
  def adjacency_list_to_incidence_matrix(adjacency_list):
    ''' Parameters
    ----------
    adjacency_matrix : list[list[int]] or string
      
    formats:
      as string 
      1.  2 5 6
      2.  1 3 6
      3.  2 4 5 12
      4.  3 8 9 11
      5.  1 3 7 9
      6.  1 2 7
      7.  5 6 8
      8.  4 7 9 12
      9.  4 5 8 10
      10. 9
      11. 4
      12. 3 8
      
      as list of lists
      [[1, 4, 5],
      [0, 2, 5],
      [1, 3, 4, 11],
      [2, 7, 8, 10],
      [0, 2, 6, 8],
      [0, 1, 6],
      [4, 5, 7],
      [3, 6, 8, 11],
      [3, 4, 7, 9],
      [8],
      [3],
      [2, 7]]
      '''
    if isinstance(adjacency_list, str):
      adjacency_list = GraphRepresentationConverter.parse_adjacency_list(adjacency_list)
    
    GraphValidator.is_adjacency_list(adjacency_list)
    incidence_matrix = []

    number_of_edges = 0
    for row in adjacency_list:
      number_of_edges += len(row)
    number_of_edges //= 2

    for row in range(len(adjacency_list)):
      incidence_matrix.append([])
      for column in range(number_of_edges):
        incidence_matrix[row].append(0)

    edge = 0

    for row_index, row in enumerate(adjacency_list):
      for column in range(len(row)):
        if row[column] > row_index:
          incidence_matrix[row_index][edge] = 1
          incidence_matrix[row[column]][edge] = 1
          edge+=1

    return incidence_matrix

  @staticmethod
  def incidence_matrix_to_adjacency_list(incidence_matrix: List[List[int]]) -> List[int]:
    '''
    Converts incidence matrix to adjacency list.

    Parameters
    ----------
        incidence matrix is list of lists that are equaly long and number of inner lists are equal to their length. Inner list consists of 1 and 0 representing connection

    Returns
    -------
        adjacency list is list of lists. Length of outer list is equal to number of vertices. Inner list is empty if there is no connection to this vertex
    '''

    GraphValidator.check_incidence_matrix(incidence_matrix)

    adjacency_list = []

    #stworzenie listy
    for row in range(len(incidence_matrix)):
      adjacency_list.append([])

    for column_index, column in enumerate(incidence_matrix[0]):
      prev = None
      for row_index, row in enumerate(incidence_matrix):
        if incidence_matrix[row_index][column_index] == 1:
          if prev is None:
            prev = row_index
            
          else:
            adjacency_list[row_index].append(prev)
            adjacency_list[prev].append(row_index)
        

    return adjacency_list

  @staticmethod
  def incidence_matrix_to_adjacency_matrix(incidence_matrix: List[List[int]]) -> List[List[int]]:
    '''
    Converts incidence matrix to adjacency matrix.

    Parameters
    ----------
        incidence matrix is list of lists that are equaly long and number of inner lists are equal to their length. Inner list consists of 1 and 0 representing connection

    Returns
    -------
        adjacency_matrix is list of lists that are equaly long and number of inner lists are equal to their length. Inner list consists of 1 and 0 representing connection
    '''

    GraphValidator.check_incidence_matrix(incidence_matrix)

    adjacency_matrix = []

    for row in range(len(incidence_matrix)):
      adjacency_matrix.append([])
      for column in range(len(incidence_matrix)):
        adjacency_matrix[row].append(0)

    for column_index, column in enumerate(incidence_matrix[0]):
      prev = None
      for row_index, row in enumerate(incidence_matrix):
        if incidence_matrix[row_index][column_index] == 1:
          if prev == None:
            prev = row_index
          else:
            adjacency_matrix[row_index][prev]= 1
            adjacency_matrix[prev][row_index]= 1

    return adjacency_matrix

  @staticmethod
  def adjacency_matrix_to_incidence_matrix(adjacency_matrix: List[List[int]]) -> List[List[int]]:
    '''
    Converts adjacency matrix to incidence matrix.

    Parameters
    ----------
        adjacency_matrix is list of lists that are equaly long and number of inner lists are equal to their length. Inner list consists of 1 and 0 representing connection

    Returns
    -------
        incidence matrix is list of lists that are equaly long and number of inner lists are equal to their length. Inner list consists of 1 and 0 representing connection
    '''

    incidence_matrix = []

    number_of_edges = 0
    for row in adjacency_matrix:
      for column in row:
        number_of_edges += column
    number_of_edges //= 2

    for row in range(len(adjacency_matrix)):
      incidence_matrix.append([])
      for column in range(number_of_edges):
        incidence_matrix[row].append(0)

    edge = 0

    for row_index, row in enumerate(adjacency_matrix):
      for column_index, column in enumerate(row):
        if row_index > column_index:
          if column == 1:
            incidence_matrix[row_index][edge] = 1
            incidence_matrix[column_index][edge] = 1
            edge+=1

    return incidence_matrix

  # fixed Brak obsługi dla żadnego formatu podobnego do opisanego w pdfie ,,Przykładowe wejście - zestaw 1
  @staticmethod
  def parse_adjacency_list(adjacency_list_string: str) -> list:
    
    splitted_list = adjacency_list_string.split('\n')

    values: list = []
    parsed_list: list = []

    for sublist in splitted_list:
        try:
            values.append(sublist.split('.')[1])
        except IndexError:
            continue
    
    for v in values:
        parsed_list.append(list(filter(None, v.split(' '))))

    for i,sublist in enumerate(parsed_list):
        for j, val in enumerate(sublist):
            parsed_list[i][j] = int(val) - 1

    return parsed_list
