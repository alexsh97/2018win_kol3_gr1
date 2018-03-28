class FlightSim(object):
  """Flight Simulator.
  
  Simulates a plane flight with orientation changing over time
  """

  def __init__(self, plane):
    self._plane = plane
    print("Flight started")


  def run(self):
    isFlying = True	
    while isFlying:
      print("Actual angle:", self._plane.getAngle())
      self._plane.increaseAngleByGaussian()
      userDecision = input("Do you want to exit the simulator?")
      if userDecision in ["quit", "q", "exit"]:
        isFlying = False
    else:
      print("Plane simulation terminated!")
      
        
	
