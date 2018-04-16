'''
__title__ = '012.异常捕捉.py'
__author__ = 'Jeffd'
__time__ = '4/16/18 11:43 AM'
'''
'''
    tips: python的异常处理机制
'''


def my_try():
    try:
        print('执行什么')
        raise KeyError
        return 1
    except KeyError as e:
        print('捕捉到异常')
        return 2
    else:
        print('没异常')
        return 3
    finally:
        print('不管有没有异常')
        return 4


if __name__ == '__main__':
    print(my_try())

'''
    结果： 
    执行什么
    捕捉到异常
    不管有没有异常
    4
    返回的值是4,try里面的return没有返回是因为抛出异常后面的return没有执行了
    except实际上执行到了，也有返回值，压入一个栈中
    然后直接到finally返回4,压入栈，打印取值的时候取到最上层的4，所以结果为4
'''
