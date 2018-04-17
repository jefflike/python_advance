'''
__title__ = '015.test.py'
__author__ = 'Jeffd'
__time__ = '4/17/18 3:31 PM'
'''
'''
    tips: bisect用于维护已排序的序列，分别insort插入和bisect返回要数据插入列表
    的位置是从左边计算起还是右边计算起。
    两者默认都是right
'''

import bisect
my_list = []
bisect.insort(my_list, 12)
bisect.insort(my_list, 313)
bisect.insort(my_list, 21)
bisect.insort(my_list, 3)
bisect.insort(my_list, 90)
bisect.insort(my_list, 123)
print(my_list) # 结果是一串排序好了的序列 [3, 12, 21, 90, 123, 313]
print(bisect.bisect_left(my_list, 313)) # 5
print(bisect.bisect_right(my_list, 313)) #6
print(bisect.bisect_left(my_list, 312)) # 5
print(bisect.bisect_right(my_list, 312))#5


# 简单来说insort_left与right在插入数据的时候，当插入的数据位置的数据与将插入数据值相等的时候
# 将值排在其左或右。比如成绩分为，优良中差，都是优的时候排序要按照分数大小排在左或右。
