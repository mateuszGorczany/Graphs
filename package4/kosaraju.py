def transpose(G):
  transposed_graph = [[0 for column in G] for row in G]
  for row_index, row in enumerate(G):
    for column_index, column in enumerate(row):
      transposed_graph[row_index][column_index] = G[column_index][row_index]
  return transposed_graph

def make_list_vertices_sorded_by_time_desc(f):
  f_with_indexes = [(vertex_index, vertex) for vertex_index, vertex in enumerate(f)]

  vertices_sorded_by_time_desc = [vertex_index for vertex_index, time in sorted(f_with_indexes, key=lambda elem : elem[1])]
  vertices_sorded_by_time_desc.reverse()

  return vertices_sorded_by_time_desc

def kosaraju(G):
  d = [-1 for vertex in G]
  f = [-1 for vertex in G]
  comp = [-1 for vertex in G]
  
  t = [0]
  for vertex, _ in enumerate(G):
    if d[vertex] == -1:
      DFS_visit(vertex, G, d, f, t)
  GT = transpose(G)
  nr = 0

  vertices_sorded_by_time_desc = make_list_vertices_sorded_by_time_desc(f)

  for vertex in vertices_sorded_by_time_desc:
    if comp[vertex] == -1:
      nr = nr + 1
      comp[vertex] = nr
      Components_R(nr, vertex, GT, comp)
  
  return comp




def DFS_visit(v, G, d, f, t):
  t[0] = t[0] + 1
  d[v] = t[0] 
  for u, _ in enumerate(G):
    if G[u][v] == 1 and d[u] == -1:
      DFS_visit(u, G, d, f, t)
  t[0] = t[0] + 1
  f[v] = t[0] 

def Components_R(nr, v, GT, comp):
  for u, _ in enumerate(GT):
    if GT[u][v] == 1 and comp[u] == -1:
      comp[u] = nr
      Components_R(nr, u, GT, comp)