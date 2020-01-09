from add_test import Rectangle


class Rectangle3(Rectangle):
	
	def __gt__(self, other):
		if not isinstance(other, Rectangle3):
			raise TypeError('>比较要求目标是Rectangle')
		return True if self.width*self.height > other.width*other.height else False
		
	def __eq__(self, other):
		if not isinstance(other, Rectangle3):
			raise TypeError('==比较要求目标是Rectangle3')
		return True if self.width*self.height == other.width*other.height else False
		
	def __ge__(self, other):
		if not isinstance(other, Rectangle3):
			raise TypeError('>-比较要求目标是Rectangle3')
		return True if self.width*self.height >= other.width*other.height else False
		
		
if __name__ == "__main__":
	r1 = Rectangle3(4, 5)
	r2 = Rectangle3(3, 4)
	
	print(r1 > r2)
	print(r1>=r2)
	print(r1<r2)
	print(r1<=r2)
	print(r1==r2)
	print(r1!=r2)
	print('--------------')
	r3 = Rectangle3(2, 6)
	print(r2>=r3)
	print(r2>r3)
	print(r2<=r3)
	print(r2<r3)
	print(r2==r3)
	print(r2 != r3)