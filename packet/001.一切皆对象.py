'''
__title__ = '001.一切皆对象.py'
__author__ = 'Jeffd'
__time__ = '4/14/18 8:43 AM'
'''
'''
tips: 类和函数都是python中的一等对象。
怎么理解这个一等对象呢：
1.可以赋值给一个变量;
2.可以添加到集合对象（列表字典等）;
3.可以作为参数传递给函数（像实参一样的传递方式）;
4.可以作为函数的返回值（闭包使用函数名的使用方式）。
'''


# 1.可以赋值给一个变量
def new_func(name=None):
    print("i am jeff")


my_func = new_func
my_func()
# 结果： i am jeff
# 所以的出结论 函数名是可以作为参数被传递的

class new_class:
    def __init__(self, name):
        print(name + ' is pretty good')


my_class = new_class
new_class('jeff')
# 结果： jeff is pretty good
# 所以的出结论 类名是可以作为参数被传递的
# 即可以赋值给一个变量


# 可以添加到集合对象（列表字典等）
new_list = [my_func, my_class]
for item in new_list:
    item('jeff')

# 结果：i am jeff
# jeff is pretty good
# 将函数名和类名加入到序列对象，可继续使用
# 即可以添加到集合对象


# 3.可以作为参数传递给函数（像实参一样的传递方式）
def name_func(name=None):
    name('jeff')


name_func(new_func)
# 结果：i am jeff
# 函数名可以作为参数传递，同理可得类名也相同
# 即可以作为参数传递给函数


# 4.可以作为函数的返回值（闭包使用函数名的使用方式）
def ret_func():
    print("这是一个返回函数")
    return new_func


func = ret_func()
func('jeff')
# 结果：这是一个返回函数
# i am jeff
# 这类似于闭包函数，当然类名也是可以当作变量名来传递的
# 所以可是可以当作函数的返回值进行返回
# 即可以作为函数的返回值

# 综上所述，函数与类符合python的一等对象的所有特征
# 所以我们认为，函数与类是python的一等对象