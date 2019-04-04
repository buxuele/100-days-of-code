# when: 2019/04/04 11:21 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

# 单例模式？？？
# def singleton(cls):
#     ins = {}
#     def wrapper(*args, **kwargs):
#         if cls not in ins:
#             ins[cls] = cls(*args, **kwargs)
#         return ins[cls]
#     return wrapper
#
#
# @singleton
# class Foo(object):
#     pass
#
# foo1 = Foo()
# foo2 = Foo()
# if foo1 is foo2:
#     print("ok")
#
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_ins'):
#             cls._ins = super(Singleton, cls).__new__(cls, *args, **kwargs)
#         return cls._ins
#
# class Foo(Singleton):
#     pass


# type 是python的元类， 是用于创建类对象的类，实例化时必须实现__call__方法。
class Singleton(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '_ins'):
            cls._ins = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._ins

class Foo(object):
    __metaclass__ = Singleton


foo1 = Foo()
foo2 = Foo()
if foo1 is foo2:
    print("ok")















