"""
这是我们编写的第一个模块，该模块包含以下内容
my_book: 字符串变量
say_hi:简单的函数
User: 代表用户的类
"""

print('这是module 1')
my_book = '疯狂python讲义'

def say_hi(user):
	print('%s,你好，欢迎学习Python'% user)
	
class User(object):
	def __init__(self, name):
		self.name = name
	def walk(self):
		print('%s正在慢慢地走' % self.name)
		
	def __repr__(self):
		return 'User[name=%s]'%self.name
		

# test code
def test_my_book():
	print(my_book)
	
def test_say_hi():
	say_hi('孙悟空')
	say_hi(User('Charlie'))
	
def test_User():
	u = User('白骨精')
	u.walk()
	print(u)

	
if __name__ == "__main__":
	test_my_book()
	test_say_hi()
	test_User()