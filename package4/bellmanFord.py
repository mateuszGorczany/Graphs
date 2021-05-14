   
class BellmanFord:
  
  def __init__(self, G, w, s):
    self.ds = [float("inf") for vertex in G]
    self.ps = [None for vertex in G]
    self.ds[s] = 0
    self.G = G
    self.w = w
    self.s = s

    if not self.__solve():
      raise Exception("Negative weights found")

  def __solve(self):
    for i in range(1,len(self.G)-1):
    #   print(i)
    #   print(self.ds)
    #   print(self.ps)
    
      for u, _ in enumerate(self.G):
        for v, _ in enumerate(self.G[u]):
          if self.G[u][v]==1:
            self.__Relax(u, v)
    for u, _ in enumerate(self.G):
      for v, _ in enumerate(self.G[u]):
        if self.G[u][v]==1 and self.ds[v] > self.ds[u] + self.w[u][v]:
          return False
    return True

  def __Relax(self, u, v):
    if self.ds[v] > self.ds[u] + self.w[u][v]:
      self.ds[v] = self.ds[u] + self.w[u][v]
      self.ps[v] = u
  
  def print_result(self):
      '''
        Prints weight and route for each vertex. Route starts at vertex s.
      '''
      print(f'START s = {self.s}')
      for i, weight in enumerate(self.ds):
        path_list = []
        path_index = i
        try:
          while path_index != self.s:
            if self.ps[path_index] == None:
              raise Exception()
            path_list.append(path_index)
            path_index = self.ps[path_index]
          path_list.append(self.s)
          path_list.reverse()
          print(f'd({i})\t= {weight} ==> {path_list}')
        except:
          print(f'd({i})\t= None')
