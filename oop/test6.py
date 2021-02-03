class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
class GraduateStudent(Student):
    # __slots__ = ()
    pass

g = GraduateStudent()
g.score = 99
print(g.score)