'''
__title__ = '011.python使用的继承方式mixin.py'
__author__ = 'Jeffd'
__time__ = '4/16/18 10:18 AM'
'''
'''
    tips: super的调用是按照的mro的顺序进行的，但是实际写的时候，尤其是框架
    这样写很容易让人混乱，即写着写着，逻辑就不是按照你想得那样走的了。
    以drf的源码为例，drf设计了mixins，mixins设计的时候，每种mixin都只做一件事，例如
    listmixin就只列出所有的列表，retrieve mixin就做显示详细。功能单一。
'''
'''
    mixin的模式就是写一个mixin的类，然后在其下创建的类都打散
    特点：
    1. 功能单一
    2. 不和基类关联，mixin和viewset结合继承。不同的mixin与viewset进行搭配
        可以和任意的基类进行组合，不需要mixin也可以完成初始化
    3. 在mixin中不要使用super。
'''