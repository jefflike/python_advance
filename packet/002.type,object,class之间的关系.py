'''
__title__ = '002.type,object,class之间的关系.py'
__author__ = 'Jeffd'
__time__ = '4/14/18 9:25 AM'
'''
'''
tips: 更好的理解python中一切接对象的设计理念
关于python中type，class，object三者之间有什么样的关系
所有的对象都是由type生成的（包括type自己都是由type类抽象出来的和object）
所有的class都继承了object类（type都继承了object，只有object自己没有继承自己）
'''


# type一方面可以生成一个类，同时我们操作它查看一个对象的类型。
a = 1
print(type(a))
# 结果： <class 'int'>
# 那么1则是由int这个类生成的，那么int对象是由谁生成的呢？
print(type(int))
# 结果： <class 'type'>
# int对象是由type类生成的
# 那么type对象是由谁生成的
print(type(type))
# 结果： <class 'type'>
# type对象也是由type类生成的（c实现比较容易，类似指针指向的操作）
# type是用来生成类的，所有的类都是由类生成的

# object是python所有类都要继承的顶级基类
print(int.__bases__)
# 结果： (<class 'object'>,)
print(type.__bases__)
# 结果： (<class 'object'>,)
print(type(object))
# 结果： ()
print(object.__bases__)
# object是由type类生成的，而type类又继承了object


# type类实例化出所有对象，所有的类都继承了object
# type既是一个类又是一个对象，type对象就是type类实例化出来的
# python对象就是由type类生成的