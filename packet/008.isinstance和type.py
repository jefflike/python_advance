'''
__title__ = '008.isinstance和type.py'
__author__ = 'Jeffd'
__time__ = '4/15/18 3:18 PM'
'''
'''
    tips: isinstance用来判断一个对象是不是一个类型。
'''


class A:
    pass


class B(A):
    pass


b = B()
# 两者都是Ture
'''
    isinstance内部会进行很多操作判断出b对象属不属于另一个类
'''
print(isinstance(b, B))
print(isinstance(b, A))

# type只能判断实例b属于B类，比isinstance不精确，并不能根据继承关系找到继承的A类
print(type(b) is B)
print(type(b) is A)

'''
    所以得出结论，如果需要判断实例的类属性，使用isinstance更加精确
'''