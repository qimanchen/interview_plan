def get_mul_sum(n):
	mul_sum = 1
	i = 1
	while mul_sum != n:
		yield mul_sum
		i += 1
		mul_sum += i
	
	
if __name__ == "__main__":
	a = get_mul_sum(5)
	print(next(a))
	print(next(a))
	print(next(a))
	print(next(a))
	print(next(a))
	