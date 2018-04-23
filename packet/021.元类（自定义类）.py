'''
__title__ = '021.元类（自定义类）.py'
__author__ = 'Jeffd'
__time__ = '4/23/18 4:12 PM'
'''
'''
    tips:
    如何动态的生成一个类
'''
# def creat_class(name):
#     '''
#         自定义一个类，创建在local下的类
#     '''
#     if name == 'user':
#         class User:
#             def __str__(self):
#                 return name
#         return User
#     else:
#         class Company:
#             def __str__(self):
#                 return name
#         return Company
#
#
# if __name__ == '__main__':
#     my_class = creat_class('user')
#     print(my_class())


# type创建类
# class base_class:
#     def __init__(self):
#         self.age = 25
#
#
# def say(self):
#     return 'my name is jeffd'
#
#
# if __name__ == '__main__':
#     # 自定义的全局动态类
#     User = type('User', (base_class,), {'name': "jeffd", 'say': say})
#     user = User()
#     print(user.name) # jeffd
#     print(user.say()) # my name is jeffd
#     print(user.age) # 25
#
#     '''
#     简单来说创建类的类就叫做元类
#     '''
'''
    python中的类实例化过程，创建一个类User如果类没有metaclass，那么它会
    调用type来生成一个类，这个类对象再去实例化生成一个obj
    如果定义了metaclass，那么会用这个元类来实例化我们的类对象
    如果自己没有定义但是父类调用了metaclass，就会用父类的metaclass生成类对象
    按照mro查找到上游都没有定义metaclass就会调用type生成类对象
    所以metaclass的优先级比较高
'''


class Metaclass(type):
    '''
    继承type，创建类的类所以是元类，控制User的创建
    '''
    def __new__(cls, *args, **kwargs):
        '''
        args里就是类似type()创建类的三个参数，类名，基类和dict
        :param args:
        :param kwargs:
        :return:
        '''
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=Metaclass):
    '''

    '''
    pass