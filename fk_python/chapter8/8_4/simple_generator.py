def test(val, step):
	print('---- function start running -----')
	cur = 0
	
	for i in range(val):
		cur += i * step
		yield cur
		
		
if __name__ == "__main__":
	# # t = test(10,2)
	
	# print('======')
	# print(next(t))
	# print(next(t))
	t = test(10, 1)
	print(list(t))
	t = test(10,3)
	print(tuple(t))