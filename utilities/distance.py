from package3.dijkstra import Dijkstra

def create_distance_matrix(G):
  '''
    G is weight matrix. Weight matrix is adjacency matrix with weights (integer greater than 0) instead of ones in elements indicating connection.
  '''
  distance_matrix = []
  for i, _ in enumerate(G):
    dijkstra = Dijkstra(G, i)
    dijkstra.solve()
    distance_matrix.append(dijkstra.d)
  return distance_matrix