class Point:
	def __init__(self, x: float, f: float):
		self.x = x
		self.f = f

	def __str__(self):
		return f'x : {self.x} f : {self.f}'
