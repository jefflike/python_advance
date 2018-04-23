'''
__title__ = '018.上下文实现与管理.py'
__author__ = 'Jeffd'
__time__ = '4/18/18 3:19 PM'
'''
'''
    tips: http://www.cnblogs.com/Jeffding/p/8759430.html
    我们自己实现一个上下文管理器会考虑使用魔法方法__enter__与__exit__，
    但是我们想将一个原本不是上下文管理器的类实现遵循上下文协议的方式
    那么我们需要使用到contextmanager，管理上下文
'''


# 举个例子看看他有什么作用
class MyResource:
    '''
    我们查询数据库进行的上下文管理操作
    '''
    def __enter__(self):
        print("查询开始")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("查询结束")

    def query(self):
        print("查询中")


with MyResource() as f:
    f.query()


# 查询数据操作如果是调用别人的接口，我们要对此操作进行类似上下文的操作
from contextlib import contextmanager


class MyResource:
    def query(self):
        print("查询中")

@contextmanager
def make_myresource():
    print("查询开始")
    yield MyResource()
    print("查询结束")

# 这里的f是yield后面返回的实例
with make_myresource() as f:
    f.query() # 插入到yield处

# 关于异常处理的管理可以参照我的博客，地址在页面上