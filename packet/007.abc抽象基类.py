'''
__title__ = '007.abc抽象基类.py'
__author__ = 'Jeffd'
__time__ = '4/15/18 2:22 PM'
'''
'''
    tips: python与java等静态语言不同，他并不需要继承某一个类或接口获得某些特性。
    而是实现某些魔法函数从而就有某种特性.
    abc抽象基类需要定义一个基础类，继承这个类的类需要定义这个基础类里所实现的所有的方法
    抽象基类本身是不可以进行实例化的。
    
'''


# 检查一个类是否实现了某种方法
a = [1, 2, 3]
# 可以看出列表实例a实现了方法__len__，所以可以调用len()方法
print(hasattr(a, '__len__'))

'''
    但是我们在判断一个实例是否属于什么类型的时候，我们更倾向直接判断这个实例是不是
    属于什么类的。类似使用instance
'''
from collections.abc import Sized
print(isinstance(a, Sized))
'''
class Sized(metaclass=ABCMeta):

    __slots__ = ()

    @abstractmethod
    def __len__(self):
        return 0

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Sized:
            if any("__len__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented
Sized内部实现了__len__方法
'''


import abc
# 1. 当我们需要判断某个对象的类型会使用抽象基类
# 2. 当我们强制子类必须实现某些方法需要使用抽象基类
class cache_basic(metaclass=abc.ABCMeta):
    '''
    如果我的子类没有实现我的定义借口的方法，那么我需要抛出异常
    当然我可以抛异常，但是我选择定义抽象基类
    '''
    @abc.abstractmethod
    def get(self, key):
        '''
        具体实现怎么缓存由子类选择，我只提供借口
        :param key:
        :return:
        '''
        pass

    @abc.abstractmethod
    def set(self, key, value):
        '''
        具体实现怎么缓存由子类选择，我只提供借口
        :param key:
        :return:
        '''
        pass


class redis_cache(cache_basic):
    pass


# 此时会抛出异常，实例化是就强制需要实现基类定义的方法
redis_cache()