def import_func1():
    print("func1")

def import_func2():
    print("func2")

#如果__all__中包含了未定义的名称，那么在执行
#import语句时会产生AttributeError
__all__ = ['import_func1','import_func2']
