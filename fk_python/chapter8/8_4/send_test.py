def square_gen():
	i = 0
	out_val = None
	while True:
		out_val = (yield out_val **2) if out_val is not None else (yield i ** 2)
		if out_val is not None: print("====%d" % out_val)
		i += 1
		
		
if __name__ == "__main__":
	sg = square_gen()
	print(sg.send(None))
	print(next(sg))
	print('------------------')
	print(sg.send(9))
	print(next(sg))
	# sg.throw(ValueError)
	sg.close()
	print(next(sg))