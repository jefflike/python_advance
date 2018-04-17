'''
__title__ = '016.不要轻易继承python的基本数据结构.py'
__author__ = 'Jeffd'
__time__ = '4/17/18 5:27 PM'
'''
'''
    tips: 这里尤其是不建议继承list，dict等底层是c语言实现的一些函数。
'''

class my_dict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)


d = my_dict(a=1)
print(d) # {'a': 1}
# def __setitem__(self, *args, **kwargs): # real signature unknown
#     """ Set self[key] to value. """
#     pass
# dict底层并没有return什么值，所以上面这种方式的继承是不生效的，v并不是我们想要的值

d['a'] = 1
print(d) # {'a': 2}
# 因为底层是c写的，某些情况下并不会出发继承关系
# 如果一定要继承，就继承


from collections import UserDict


class my_dict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value*2)


e = my_dict(a=1)
print(e) # {'a': 2}

