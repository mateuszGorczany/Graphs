import matplotlib.pyplot as plt
import math
import numpy
import random
from typing import List

from utilities.GraphValidator import GraphValidator
from utilities.Vector2d import Vector2d
from utilities.constants import TAU


class GraphPloter:
  """
  Class object allows to draw circular representation of the graph
  """
  def __init__(self, matrix, radius=10):
    GraphValidator.check_adjacency_matrix(matrix)
    self.circle = plt.Circle((0, 0), radius, fill=False)
    self.n_vertices = len(matrix)
    self.nodeRadius = 1
    self.radius = radius
    self.angle = TAU/self.n_vertices
    self.nodes = []
    self.ax = plt.gca()
    self.ax.set_xlim((-1.5*self.radius, 1.5*self.radius))
    self.ax.set_ylim((-1.5*self.radius, 1.5*self.radius))
    self.matrix = matrix

    self.add_nodes()

  def add_nodes(self):
    """
    Adds nodes to graph
    """
    node = Vector2d(0, self.radius)
    for vertice in range(self.n_vertices):
      self.nodes.append(
          node
      )
      node = node.rotate(-self.angle)

  def loadMatrix(self, matrix) -> None:
    """
    Allows to change stored adjacency_matrix
    """
    GraphValidator.check_adjacency_matrix(matrix)
    self.matrix = matrix

  def add_lines(self):
    """
    Adds edges to a graph
    """
    for i in range(1, self.n_vertices):
      for j in range(i):
        if self.matrix[i][j] == 1:
          x1, y1 = self.nodes[i].to_array()
          x2, y2 = self.nodes[j].to_array()
          plt.plot([x1,x2], [y1,y2], color="b", zorder=-1)
    return self

  def writeNumbers(self, x, y, num):
    """
    Writes numbers on nodes
    """
    visibleNumber = num
    self.ax.text(x, y, f" {visibleNumber}", color="w") if visibleNumber < 10 else self.ax.text(x, y, f"{visibleNumber}", color="w") 

  def draw(self):
    """
    Draws graph
    """
    self.add_lines()
    self.ax.add_patch(self.circle)

    for i, node in enumerate(self.nodes):

      # rusuje kółka
      self.ax.add_patch(
          plt.Circle((node.x, node.y), self.nodeRadius)
          )
      self.ax.add_patch(
          plt.Circle((node.x, node.y), self.nodeRadius, color='r', fill=False)
          )
      # rysuje liczby
      
      self.writeNumbers(node.x - self.nodeRadius/1.75, node.y - self.nodeRadius/2, i)

    plt.axis("off")
    plt.rcParams['figure.dpi'] = 200
    plt.show()