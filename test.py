#arorias

import unittest
from FlightSim import FlightSim
from Plane import Plane

class MyTesting(unittest.TestCase):
	
	def setUp(self):
		self.plane = Plane()

	def test_getAngle(self):
		self.assertEqual(self.plane.getAngle(),0.0)

	def test_Plane_init(self):
		plane = Plane()
		self.assertEqual(plane._angle, 0.0)

	def test_increaseAngleByGaussian(self):
		self.plane.increaseAngleByGaussian()
		self.assertTrue(self.plane.getAngle() < 10 or self.plane.getAngle() > 0)





