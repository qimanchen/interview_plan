from add_test import Rectangle


class Rectangle1(Rectangle):
	
	def __radd__(self, other):
		if not (isinstance(other, int) or isinstance(other, float)):
			raise TypeError("+运算要求目标是数值")
		return Rectangle1(self.width + other, self.height+other)
		
		
if __name__ == "__main__":
	r1 = Rectangle1(4, 5)
	r = 3+ r1
	print(r)