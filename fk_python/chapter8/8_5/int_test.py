from add_test import Rectangle


class Rectangle5(Rectangle):
	
	def __int__(self):
		return int(self.width*self.height)
		
		
if __name__ == "__main__":
	r = Rectangle5(4, 5)
	print(int(r))