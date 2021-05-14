def find_bridges_DFS(adjacency_matrix,vertex, parent_vertex, current_vertex, D):
    temp = 0
    D[vertex] = current_vertex
    Low = current_vertex
    current_vertex+=1
    for i in range(len(adjacency_matrix)):
      if adjacency_matrix[vertex][i] and i != parent_vertex:
        if not D[i]:
          temp = find_bridges_DFS(adjacency_matrix, i, vertex, current_vertex, D)
          if temp < Low:
            Low = temp
        elif D[i] < Low:
          Low = D[i]
    
    if parent_vertex > -1 and Low == D[vertex]:
      adjacency_matrix[parent_vertex][vertex] = adjacency_matrix[vertex][parent_vertex] = 2

    return Low