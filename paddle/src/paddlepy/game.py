from Vector import Vector
class Paddle:

	SPEED = 0.01

	def __init__(self, pos = Vector([0,0]), vel = Vector([0,0]), acc=Vector([0,0])):
		self.pos = pos
		self.vel = vel
		self.acc = acc

	def step(self):
		self.pos += (SPEED*self.vel[0], SPEED*self.vel[1])


