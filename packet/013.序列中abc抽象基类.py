'''
__title__ = '013.序列中abc抽象基类.py'
__author__ = 'Jeffd'
__time__ = '4/17/18 9:52 AM'
'''
'''
    tips: 与容器相关的数据结构相关的抽象基类，是在collections下的abc中的
    与序列相关的两个是，"Sequence"(不可变), "MutableSequence"（可变）,
'''


from collections import abc
# __all__函数定义了所有的抽象基类的名称
# Sequence(Sized, Iterable, Container)
# Sized实现:
# @abstractmethod
#     def __len__(self):
#         return 0
# 所以不可变类型可以实现len()获取长度
# Iterable实现迭代
# Container
#    @abstractmethod
#     def __contains__(self, x):
#         return False
# __contains__方法可以进行in判断，除了他__getitem__也可以in判断
'''
class MutableSequence(Sequence):

    __slots__ = ()

    """All the operations on a read-write sequence.

    Concrete subclasses must provide __new__ or __init__,
    __getitem__, __setitem__, __delitem__, __len__, and insert().

    """

    @abstractmethod
    def __setitem__(self, index, value):
        raise IndexError

    @abstractmethod
    def __delitem__(self, index):
        raise IndexError
可变的序列抽象基类就是实现了这些item魔法函数，才具有可变的基础，其是继承了Sequence作为基础类
'''
# 对于可变的序列实现了+=，extend，append函数
'''
def __iadd__(self, values):
    self.extend(values)
    return self
+=实际上就是调用了extend方法，
def extend(self, values):
    'S.extend(iterable) -- extend sequence by appending elements from the iterable'
    for v in values:
        self.append(v)
extend实际上就是遍历append。
@abstractmethod
def insert(self, index, value):
    'S.insert(index, value) -- insert value before index'
    raise IndexError

def append(self, value):
    'S.append(value) -- append value to the end of the sequence'
    self.insert(len(self), value) 
'''


a = [1]
a.append((1, 2))
print(a) # [1, (1, 2)]
b = [1]
b.extend((1, 2))
print(b) # [1, 1, 2]
c = [1, 2]
c[1:1] = [3, 4]
print(c)