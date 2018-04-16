'''
__title__ = '010.super的调用顺序.py'
__author__ = 'Jeffd'
__time__ = '4/15/18 6:30 PM'
'''
'''
    tips: super继承的机制，也是遵循了广度优先，mro的算法。
'''


class father:
    def __init__(self):
        print('i am father')


class son(father):
    def __init__(self):
        print('i am son')
        super().__init__()


if __name__ == '__main__':
    son()
# 结果： i am son
# i am father
# 儿子继承了父亲的资产
# 这里只是一个简单的继承关系，那么对于多继承关系，super函数是如何执行的呢


class A:
    def __init__(self):
        print('it is A')


class B(A):
    def __init__(self):
        print('it is B')
        super().__init__()


class C(A):
    def __init__(self):
        print('it is C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('it is D')
        super().__init__()


if __name__ == '__main__':
    D()
    print(D.__mro__)

'''
    结果： 
    it is D
    it is B
    it is C
    it is A
    实例化D，super执行到他的父类B，B有super继承于A，但是结果下一步并没有执行
    A，而是回到C，最后执行到A，与mro()广度优先的算法结果是一致的
    (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
'''
