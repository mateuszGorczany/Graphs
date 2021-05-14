from package4.digraphGNP import GNP
from package4.bellmanFord import BellmanFord

def johnson(G: GNP, w):
    BellmanFord(G, w, G.n_verticies-1)