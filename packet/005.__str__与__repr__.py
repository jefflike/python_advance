'''
__title__ = '__str__与__repr__.py'
__author__ = 'Jeffd'
__time__ = '4/14/18 3:48 PM'
'''
'''
tips: __str__延伸了可读性，经常在使用print打印的时候看到的就是__str__
__repr__是开发使用项，
'''


class new_class:
    pass


my_class = new_class()
print(my_class) # <__main__.new_class object at 0x7fe7de5a9898>
print(str(my_class)) # <__main__.new_class object at 0x7fe7de5a9898>
# 此时打印的字符串的格式默认就是调用了str方法的


class new_class:

    def __str__(self):
        return '调用打印方法就是调用了我'


my_class = new_class()
my_class # 交互式环境打印依然是<__main__.new_class object at 0x7fe7de5a9898>
print(my_class) # 调用打印方法就是调用了我
print(str(my_class)) # 调用打印方法就是调用了我
# 使用__str__使得查看类实例更加易懂，my_class本身依然是类的实例对象而不是字符串


class new_class:

    def __repr__(self):
        '''
        可以写到任意我们定义的类中
        :return:
        '''
        return '直接打印方法就是调用了我'

my_class = new_class()
my_class # 在解释器环境下是可以打印此种类型的，其直接调用的是__repr__
my_class.__repr__() # 上面相当于调用了此种方法
# 在交互式环境中打印的就是： '直接打印方法就是调用了我'