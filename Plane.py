import random

class Plane(object):
  """Plane representation.
  
  Represents a plane which is changing the angle between wings
  and earth during flight with gaussian distribution.
  """
  def __init__(self):
    self._angle = 0.0

  def increaseAngleByGaussian(self):
    self._angle += random.gauss(0, 10)

  def getAngle(self):
    return self._angle
	
