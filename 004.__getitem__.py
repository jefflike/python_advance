'''
__title__ = '004.关于魔法函数.py'
__author__ = 'Jeffd'
__time__ = '4/14/18 10:31 AM'
'''
'''
tips: python的魔法函数
格式一般是__xx__，并且我们最好是不要自己定义魔法函数，而是去使用python自己的魔法函数
并且python的魔法函数足够多，足够我们使用了
'''


#1.__getitem__
class friend:
    def __init__(self, my_list):
        self.my_friend = my_list


my_friend = friend(['jeff', 'frank', 'xixi'])
for item in my_friend.my_friend:
    print(item)

# 使用魔法函数
class friend:
    def __init__(self, my_list):
        self.my_friend = my_list

    def __getitem__(self, item):
        return self.my_friend[item]

    def __len__(self):
        '''
        由此方法的类才可以调用len()
        :return:
        '''
        return len(self.my_friend)

my_friend = friend(['jeff', 'frank', 'xixi'])
for item in my_friend:
    print(item)

my_friend1 = my_friend[:2]
for item in my_friend1:
    print(item)
# 没有__len__会报错
print(len(my_friend))
# 没有__getitem__会报错
print(len(my_friend1))

# 值得一提的是python内置对象（可迭代的对象，本质是c实现的）调用len()方法的时候是不会遍历方法的，
# 比如对于列表的len()操作，实际上在此数据结构的头部保存了列表的数值
# 读取的时候直接取出头部长度显示即可。
