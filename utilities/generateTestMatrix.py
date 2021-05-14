import random

def generateTestMatrix(size):
  matrix = [[random.randint(0,1) for _ in range(size)] for _ in range(size)]
  for i in range(1, size):
    for j in range(i):
      matrix[i][j] = matrix[j][i]
  for i in range(size):
    matrix[i][i] = 0
  
  return matrix