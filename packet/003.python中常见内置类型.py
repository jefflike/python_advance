'''
__title__ = '003.python中常见内置类型.py'
__author__ = 'Jeffd'
__time__ = '4/14/18 10:05 AM'
'''
'''
tips: 对象的特征： 1.身份（id）2.类型，3.值
主要说python中对象的类型
'''


# 1. 对象的身份
a =1
print(id(a))
# 结果： 94882010435200
# 即任意对象都是有id的


# 2.类型（任意对象都是有类型的）
# None类型，python解释器启动是None类会生成一个None对象
# 并且全局只有一个None对象
a = None
b = None
print(a is b)
# 结果： Ture
# 全局只有一个None对象


# 数值类型
# int，float，complex，bool


# 迭代类型，可用for循环遍历


# 序列类型
# list，bytes、bytearray、memoryview，range，tuple，str，array


# 映射类型（k，v）


# 集合类型
# set， frozenset


# 上下文管理类型（with）


# 其他类型
# 还有很多其他类型，后面使用到介绍


# 3.值（对象都对应一个值）