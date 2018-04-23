'''
__title__ = '019.__getattr__、__getattribute__.py'
__author__ = 'Jeffd'
__time__ = '4/22/18 7:08 AM'
'''
'''
    tips: __getattr__,查找不到属性的时候调用
    
'''
class Friend:
    def __init__(self):
        self.name = 'jeffd'
        self.gender = 'male'

    def __getattr__(self, value):
        return 'not defined'


f = Friend()
print(f.name) # jeffd
print(f.age) # not defined
'''
    当属性不存在的时候会触发__getattr__
'''

class Others:
    def __init__(self, dic):
        self.dic = dic

    def __getattr__(self, value):
        return self.dic[value]

    # def __getattribute__(self, item):
    #     '''
    #     优先返回此属性，不论你的属性能不能找到，都返回他
    #     尽量不重写它，
    #     :param item:
    #     :return:
    #     '''
    #     return 'nothing'


o = Others({'name': 'jeffd', 'gender': 'male'})
print(o.name)