from add_test import Rectangle


class RectangleRound(Rectangle):
	def __round__(self, ndigits=0):
		self.width, self.height = round(self.width, ndigits), round(self.height, ndigits)
		return self

		
if __name__ == "__main__":
	r = RectangleRound(4.13, 5.56)
	result = round(r, 1)
	print(r)
	print(result)