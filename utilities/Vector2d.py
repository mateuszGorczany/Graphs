import numpy as np

class Vector2d:
  """
  Class object represents vector and allows performing basic vector operations
  """
  def __init__(self, x=0., y=0.):
    self.x = x
    self.y = y

  def rotate(self, angle):
    """
    Rotates self object by the given :angle
    """
    return Vector2d(
        self.x*np.cos(angle) - self.y*np.sin(angle), 
        self.x*np.sin(angle) + self.y*np.cos(angle)
    )
  
  def __repr__(self):
    return f"[{self.x}, {self.y}]"

  def to_array(self):
    """
    Returns
    -------
     Vector coordinates as an array [x,y]
    """
    return [self.x, self.y]