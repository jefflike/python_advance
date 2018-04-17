'''
__title__ = '006.鸭子类型与多态.py'
__author__ = 'Jeffd'
__time__ = '4/14/18 4:39 PM'
'''
'''
tips:鸭子类型就是，当看到一只鸟走起来像鸭子，游泳像鸭子，叫起来也像鸭子
那么这只鸟就可以称作鸭子
python的多态性就是基于鸭子类型的
'''


# 在python中具有同样的方法的类我们可以把他归并成一类事物
class turtle:

    def swim(self):
        print('turtle swimming')


class duck:

    def swim(self):
        print('duck swimming')


class goose:

    def swim(self):
        print('goose swimming')


class swim_pig:

    def swim(self):
        print('swim_pig swimming')


# 这几个动物都具有相同的方法，即都会游泳，那么我们可以把他看作一类
fish = duck
fish().swim() # duck swimming
# 如果我根据他们都会游泳把他叫做鱼类型，这就是鸭子类型
# 通过魔法函数，对象可以72变，比如本来是鸡，但是通过定义魔法函数，就变成了鸭子
'''
面向对象的java实现鸭子类型是基于继承完成的
写一点java的伪代码
class fish:

    def swim(self):
        print('fish swimming')
        

class swim_pig(fish):

    def swim(self):
        print('swim_pig swimming')
        
fish sw = swim_pig()
sw.swim()
结果就是swim_pig swimming
'''

# python与java不同的地方就在于，我们不需要静态指明类型
# sw不必须指定为fish类型，python语言本身就自带多态性的


fish_list = [turtle, duck, goose, swim_pig]
# 我们把这些都具有游泳方法的类归并为fish_list，即鱼一类
for fish in fish_list:
    fish().swim()


# 这种多态思维是构建python语法的基础
'''
    python的多态性，是贯穿整个语言的，比如我们根据python的自定义类型可以将
    python的类型进行划分，比如我们对具有__iter__方法的对象，我们就称他为可迭代
    对象，那么对于这类方法我们可以对他们进行各种的迭代操作，具有__iter__方法的类
    我们就根据这个特征将他们归并为一类。
    def extend(self, iterable): # real signature unknown; restored from __doc__
        """ L.extend(iterable) -> None -- extend list by appending elements from the iterable """
        pass
    举例子：
    上面是[]的扩展方法，[].extend()方法传人的参数不仅仅是列表类，而是所有实现了
    __iter__方法的类，即所有可迭代对象都可以作为参数传入，这种思想贯穿了我们的python，
    python的魔法类型就是基于此使用，才使得python如此灵活
'''

