from add_test import Rectangle


class Rectangle2(Rectangle):
	
	def __iadd__(self, other):
		if not (isinstance(other, int) or isinstance(other, float)):
			raise TypeError('+=运算符要求目标是数值')
		return Rectangle2(self.width + other, self.height+other)
		
		
if __name__ == "__main__":
	r = Rectangle2(4, 5)
	r += 2
	print(r)