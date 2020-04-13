import unittest
from Vector import Vector

class TestVecMethods(unittest.TestCase):

	def test_scale(self):
		v = Vector([-2,3,4])
		w = Vector([-10.2,-8,14])
		self.assertEqual(3*v, Vector([-6,9,12]))
		self.assertEqual(3.1*v, Vector([-6.2,9.3,12.4]))
		
	def test_add(self):
		v = Vector([-2,3,4])
		w = Vector([-10.2,-8,14])
		self.assertEqual(w+v, Vector([-12.2,-5,18]))

if __name__ == '__main__':
    unittest.main()
