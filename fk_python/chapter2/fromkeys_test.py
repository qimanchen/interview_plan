# fromkeys -- 给多个key创建字典，这些key的默认value都是None
a_dict = dict.fromkeys(['a', 'b'])
#>>> a_dict = {'a': None, 'b', None}

# 改变默认值
# 使用fromkeys -- dict类直接调用
c_dict = dict.fromkeys((13, 17), 'good')
#>>> c_dict = {13: 'good', 17: 'good'} 
