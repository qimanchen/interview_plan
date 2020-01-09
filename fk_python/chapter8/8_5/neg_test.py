from add_test import Rectangle


class Rectangle4(Rectangle):
	
	def __neg__(self):
		self.width, self.height = self.height, self.width
		
		
if __name__ == "__main__":
	r = Rectangle4(4, 5)
	-r
	print(r)