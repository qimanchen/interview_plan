class Rectangle(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
	def setSize(self, size):
		self.width, self.height = size 
		
	def getSize(self):
		return self.width, self.height
		
	size = property(getSize, setSize)
	
	def __add__(self, other):
		if not isinstance(other, Rectangle):
			raise TypeError('+运算要求目标是Rectangle')
		return Rectangle(self.width + other.width, self.height + other.height)
	
	def __repr__(self):
		return 'Rectangle(width=%g, height=%g)' % (self.width, self.height)
		

if __name__ == "__main__":
	r1 = Rectangle(4, 5)
	r2 = Rectangle(3, 4)
	r = r1 + r2
	print(r)