def are_lists_the_same(a:list,b:list) -> bool:
    '''
        Checks if lists are composed of the same elements
        1,2,3 == 3,1,2
    '''
    a = sorted(a)
    b = sorted(b)
    a_set = set(a)
    b_set = set(b)
    if not a_set.difference(b_set):
        return True
    return False

def get_all_neighbours(G,v) -> list:
    '''
        returns all neighbours of vertice v in G graph
        G => adjacency matrix
        v => number of node
    '''
    neighbours = []

    for i in range(len(G)):
        if G[v][i] == 1:
            neighbours.append(i)

    return neighbours

def components(G) -> list:
    '''
        Method returns list of subcomponents of the graph
        G => adjacency matrix
    '''
    comp = [[] for _ in range(len(G))]
    final_comps = []
    visited = []
    previsited = []
    continuously_connected = []
    nr = 0
    node = 0

    neighbours = []

    while nr < len(G):
        node = nr
        while node < len(G) and node not in previsited:
            while True: 
                new_neighbours = [neighbour for neighbour in get_all_neighbours(G,node) if neighbour not in visited and neighbour not in neighbours]
                neighbours.extend(new_neighbours)
                if node not in visited:
                    visited.append(node)
                if node in neighbours:
                    neighbours.remove(node)
                if len(neighbours):
                    node = neighbours[0]
                else:
                    break

            for j in range(len(G)):
                if node in comp[j]:
                    node += 1
            neighbours.clear()
            new_neighbours.clear()
            if node < len(G):    
                comp[node].extend(visited)
            previsited.extend(visited)
            visited.clear()
        nr += 1
    for i in range(len(comp)):
        if comp[i]:
            exists = False
            for j in range(len(final_comps)):
                if are_lists_the_same(comp[i], final_comps[j]):
                    exists = True
                    break
            if not exists:
                final_comps.append(comp[i])
            
    return final_comps

def find_max_subgraph(graph_components):
    '''
    returns subgraph with the most amount of nodes
    '''
    maxComp = graph_components[0]
    for component in graph_components:
        if len(component) > len(maxComp):
            maxComp = component
    return maxComp