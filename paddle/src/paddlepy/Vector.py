# Vector Class
class Vector:

	def __init__(self, arr):
		self.arr = arr

	def __len__(self):
		return self.arr.__len__()

	def __eq__(self, other):
		return self.arr.__eq__(other.arr)

	def __mul__(self, other):
		new_arr = []
		if type(other) in (int, float):
			for x in self:
				new_arr.append(x*other)
		else:
			raise(TypeError("Not able to multiply with {}".format(type(other))))
		return Vector(new_arr)

	def __getitem__(self, key):
		return self.arr[key]

	def __add__(self, other):
		new_arr = []
		if type(other) is Vector:
			n = len(self.arr)
			m = len(other.arr)
			if m != n:
				raise(TypeError('Cannot add vectors of different dimension'))
			for i in range(m):
				new_arr.append(self[i] + other[i])
		else:
			raise(TypeError('Not able to add Vector with {}'.format(type(other))))
		return Vector(new_arr)

	def __repr__(self):
		return "Vector: {}".format(self.arr)

	def __rmul__(self, other):
		return self.__mul__(other)