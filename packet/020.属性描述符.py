'''
__title__ = '020.属性描述符.py'
__author__ = 'Jeffd'
__time__ = '4/22/18 9:25 PM'
'''
'''
    tips: 
    自定义类实现任一
    __get__, __set__, __delete__魔法方法就是属性描述符
'''


class Interger:
    '''
    数据描述符
    '''
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        '''

        :param instance, 是user的对象<__main__.User object at 0x7f6390b50f28>:
        :param value:
        :return:
        '''
        print(instance)
        if isinstance(value, int):
            if value < 0:
                raise ValueError('请输入正确年龄')
            self.value = value

        else:
            raise ValueError('请输入int类型')

    def __delete__(self, instance):
        pass


# class Interger:
#     '''
#     非数据属性描述符
#     '''
#     def __get__(self, instance, owner):
#         return self.value

class User:
    age = Interger()


user = User()
# 赋值会调用__set__方法
# user.age = '25'
user.age = 25
print(user.age)

'''
    属性查找过程
'''