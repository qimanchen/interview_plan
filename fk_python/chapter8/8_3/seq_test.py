

def check_key(key):
	
	if not isinstance(key, int): raise TypeError('index must be intger')
	if key < 0: raise IndexError('index must be not posive intger')
	if key >= 26**3: raise IndexError('index is too large')
	

class StringSeq(object):
	def __init__(self):
		self.__changed = {}
		self.__deleted = []
		
	def __len__(self):
		return 26**3
		
	def __getitem__(self, key):
		check_key(key)
		
		if key in self.__changed:
			return self.__changed[key]
		if key in self.__deleted:
			return None
		three = key //(26*26)
		two = (key - three*26*26)//26
		one = key % 26
		return chr(65+three) + chr(65+two) + chr(65+one)
		
	def __setitem__(self, key, value):
		check_key(key)
		self.__changed[key] = value
		
	def __delitem__(self, key):
		check_key(key)
		if key not in self.__deleted:
			self.__deleted.append(key)
		if key in self.__changed:
			del self.__changed[key]
			
		
if __name__ == "__main__":
	sq = StringSeq()
	
	print(len(sq))
	print(sq[26*26])
	print(sq[1])
	sq[1] = 'fkit'
	print(sq[1])
	del sq[1]
	print(sq[1])
	sq[1] = 'crazyit'
	print(sq[1])