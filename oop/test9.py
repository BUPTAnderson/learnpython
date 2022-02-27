class Foo(object):
    @classmethod
    def __new__(cls, *args, **kwargs):
        """如果不覆盖这个__new__方法,也就是说不写这个__new__方法，类会从object
        继承__new__方法完成返回值实例对象
        """
        print("__new__方法先被调用")
        tmp = super().__new__(cls, *args, **kwargs) # super().__new__与super(Foo, cls).__new__等效
        # tmp = super(Foo, cls).__new__(cls, *args, **kwargs)
        # tmp = object.__new__(cls, *args, **kwargs) # 也可以直接指定父类进行调用
        print(id(tmp))
        print(type(tmp))
        print(isinstance(tmp, Foo))
        print(issubclass(type(tmp), Foo))
        return(tmp)

    def __init__(self):
        """self是python默认传的值，该值是调用__new__的返回值"""
        print("__init__被调用")
        print(id(self))


# p = Foo()
# print(id(p))
# print(type(p))

class Bar(Foo):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        # instance = super(Bar, cls).__new__(cls, *args, **kwargs)
        # instance = super().__new__(cls, *args, **kwargs)
        instance = Foo.__new__(cls, *args, **kwargs)
        print("Bar new method")
        return instance

    def __init__(self):
        # super(Bar, self).__init__()
        # super().__init__()
        Foo.__init__(self)
        print("new Bar")


bar = Bar()
print("++++++++++++++++")


