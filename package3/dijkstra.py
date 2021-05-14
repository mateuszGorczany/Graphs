class Dijkstra:
  ''' 
    Takes weight matrix and index of starting vertex. Weight matrix is adjacency matrix with weights (integer greater than 0) instead of ones in elements indicating connection.
  '''

  def __init__(self, G, s):
    self.S = []
    self.G = G
    self.s = s

    self.d = []
    self.p = []

    for vertex in G:
      self.d.append(float('inf'))
      self.p.append(None)
    self.d[s] = 0

  def _relax(self, u, v):
    if self.d[v] > self.d[u] + self.G[u][v]:
      self.d[v] = self.d[u] + self.G[u][v]
      self.p[v] = u

  def _find_min_unready_neighbour(self):
    u_min = float('inf')
    u_min_index = 0
    for i, _ in enumerate(self.G):
      if i not in self.S:
        if u_min > self.d[i]:
          u_min = self.d[i]
          u_min_index = i
    return u_min_index

  def solve(self):
    ''' 
      Runs algorithm, and stores result in S. Elements in S represents predecessor for each vertex index (index of list corresponds to index of vertex)
    '''
    while (len(self.S) < len(self.G)):
      u = self._find_min_unready_neighbour()
      self.S.append(u)
      for neighbour, _ in enumerate(self.G[u]):
        if self.G[u][neighbour] != 0 and neighbour not in self.S:
          self._relax(u, neighbour)

  def print_result(self):
    '''
      Prints weight and route for each vertex. Route starts at vertex s.
    '''
    print(f'START s = {self.s}')
    for i, weight in enumerate(self.d):
      path_list = []
      path_index = i
      while path_index != self.s:
        path_list.append(path_index)
        path_index = self.p[path_index]
      path_list.append(self.s)
      path_list.reverse()
      print(f'd({i})\t= {weight} ==> {path_list}')