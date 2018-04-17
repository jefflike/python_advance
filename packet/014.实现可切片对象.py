'''
__title__ = '014.实现可切片对象.py'
__author__ = 'Jeffd'
__time__ = '4/17/18 2:47 PM'
'''
'''
    tips: 通过魔法函数实现一个类，具有序列的切片等功能，切片结果应为
    一个对象，这样可以完成多次切片，其功能类似于drf的queryset。
'''


class my_sequence:

    def __init__(self, new_list):
        '''
        传入一个可迭代的对象到我的序列对象中
        :param new_list:
        '''
        self.my_list = new_list

    def __reversed__(self):
        '''
        使我的序列可以迭代
        :return:
        '''
        for i in reversed(range(len(self.my_list))):
            yield self.my_list[i]

    def __contains__(self, value):
        '''
        使我的序列可以判断in
        :param value:
        :return:
        '''
        for v in self.my_list:
            if v == value:
                return True
        return False

    def __iter__(self):
        '''
        实现序列可迭代
        :return:
        '''
        i = 0
        try:
            while True:
                v = self.my_list[i]
                yield v
                i += 1
        except IndexError:
            return

    def __len__(self):
        '''
        自定义序列的长度
        :return:
        '''
        return len(self.my_list)

    def __getitem__(self, item):
        '''
        实现切片,返回依然是对象
        :param item:
        :return:
        '''
        cls = type(self)
        print(item)
        if isinstance(item, slice):
            return cls(self.my_list[item])
        elif isinstance(item, int):
            return cls([self.my_list[item]])


S = my_sequence([1, 2, 3])
# print(1 in S)
# print(list(reversed(S)))
# for item in S:
#     print(item)
# print(len(S))
print(list(S[0:2]))
print([1,2,3][slice(None,1,None)])
