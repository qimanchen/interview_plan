# setdefault -- 当某个key在字典中存在时， 不改变其值
# 当这个key不存在时，设置为默认值
cars = {'BMW': 8.5, 'BENS': 8.3, 'AUDI': 7.9}
# 会在dict中添加一个值
# setdefault -- 是有返回值得
print(cars.setdefault('PORSCHE', 9.2)) # 9.2
print(cars)

# 设置默认值， 该key在dict中存在，不会修改dict内容
print(cars.setdefault('BMW', 3.4)) # 8.5
print(cars)
