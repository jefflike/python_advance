'''
__title__ = '009.自省机制.py'
__author__ = 'Jeffd'
__time__ = '4/15/18 4:33 PM'
'''
'''
    自省是通过一定的机制查询到对象的内部结构
    __dict__与dir()
'''


class people:
    '''
    文档：定义一个人的类
    '''
    name = '人'


class student(people):
    def __init__(self, age):
        self.age = age


if __name__ == '__main__':
    jeffd = student(26)

# 我们可以使用__dict__查找我们的属性，字典在python中是十分重要的数据结构
# 所以在实现cpy时做了很多优化，
    print(jeffd.__dict__)
# 结果： {'age': 26}
    print(student.__dict__)
# 结果：{'__init__': <function student.__init__ at 0x7f2362eabd08>, '__doc__': None, '__module__': '__main__'}
    print(people.__dict__)
# 结果： {'__weakref__': <attribute '__weakref__' of 'people' objects>, '__doc__': '\n    文档：定义一个人的类\n    ', '__dict__': <attribute '__dict__' of 'people' objects>, '__module__': '__main__', 'name': '人'}
    print(jeffd.name)
# 实际上jeffd对象可以查找到name属性但是，name属性是根据广度优先查找到的
# name属性本身是属于people类的，所以jeffd实例__dict__查找不到name属性
# 即之可被jeffd对象调用，但是并不属于创建jeffd实例的类的属性
    '''
        使用这种方式就可以获取到python中类实现了哪些方式
        当然我们知道了这个方法得到的结果是一种字典的格式
        那么我们就可以通过字典方式进行赋值
    '''
    jeffd.__dict__['sex'] = 'male'
    print(jeffd.__dict__)
# 结果： {'sex': 'male', 'age': 26}
    print(dir(jeffd))
# 这种方式可以查找到jeffd实例的所有可以调用到的属性，功能呢个更为强大，查询结果是一个列表
#     print([].__dict__) # 会报错，不可以直接查看
    print(dir([]))
    # dir方法可以查看
