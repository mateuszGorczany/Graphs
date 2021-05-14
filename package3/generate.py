import random

from utilities.GenerateGraph import GenerateGraph

from package2.composition import components

def connect_components_randomly(graph:GenerateGraph, comps:list) -> GenerateGraph:
    #print(comps)
    for i,comp in enumerate(comps):
        rand_elem = random.randint(0,len(comps[i])-1)
        rand_comp = i

        while rand_comp == i:
            rand_comp = random.randint(0, len(comps)-1)

        first_node = comps[i][rand_elem]
        second_node = comps[rand_comp][random.randint(0,len(comps[rand_comp])-1)]

        graph.get_raw()[first_node][second_node] = 1
        graph.get_raw()[second_node][first_node] = 1
        #print(f'connecting {first_node} to {second_node}')
        
    return graph

def generate_random_graph():
    graph = GenerateGraph(10, 0.1)
    comps = components(graph.get_raw())
    while len(comps) > 1:
        graph = connect_components_randomly(graph, comps)
        comps = components(graph.get_raw())
    
    return graph