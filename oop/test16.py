class Foo(object):
    def __new__(cls, *args, **kwagrs):
        return object.__new__(cls, *args, **kwagrs)

    def __init__(self, name):
        print("+++++")
        self.name = name


class Bar(object):
    def __new__(cls, *agrs, **kwagrs):
        return object.__new__(Foo, *agrs, **kwagrs)


bar = Bar()
print(type(bar))  # bar其实是Foo类的实例。

# 输出为：<class '__main__.Foo'>