from utilities.distance import create_distance_matrix

def find_graph_center(G):
  '''
    G is weight matrix. Weight matrix is adjacency matrix with weights (integer greater than 0) instead of ones in elements indicating connection.
    Returns graph center and sum of its neighbours distances.
  '''
  distance_matrix = create_distance_matrix(G)
  min_vertex = 0
  min_neighbours_distance = float('inf')
  for vertex, neighbours_distance in enumerate(distance_matrix):
    neighbours_sum = sum(neighbours_distance)
    if(min_neighbours_distance > neighbours_sum):
      min_neighbours_distance = neighbours_sum
      min_vertex = vertex
  return min_vertex, min_neighbours_distance

def find_minimax_graph_center(G):
  '''
    G is weight matrix. Weight matrix is adjacency matrix with weights (integer greater than 0) instead of ones in elements indicating connection.
    Returns graph center and distance to the furthest vertex.
  '''
  distance_matrix = create_distance_matrix(G)
  min_vertex = 0
  min_max_vertex = float('inf')
  for vertex, neighbours_distance in enumerate(distance_matrix):
    max_neighbour = max(neighbours_distance)
    if(min_max_vertex > max_neighbour):
      min_max_vertex = max_neighbour
      min_vertex = vertex
  return min_vertex, min_max_vertex