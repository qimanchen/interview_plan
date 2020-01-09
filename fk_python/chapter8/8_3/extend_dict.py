class ValueDict(dict):
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
	def getkeys(self, val):
		result = []
		for key, value in self.items():
			if value == val: result.append(key)
		return result
		
	
if __name__ == "__main__":
	my_dict = ValueDict(语文=92, 数学=89, 英语=92)
	
	print(my_dict.getkeys(92))
	my_dict['编程']=92
	print(my_dict.getkeys(92))