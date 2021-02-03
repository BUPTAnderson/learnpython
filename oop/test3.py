# 函数是直接用函数名调用的
# 方法是类的一部分， python中方法看作是一个属性，属性的类型是method类
# @classmethod ：调用的时候用类名，而不是某个对象，可以看作java中的静态方法
# @property ： 像访问属性一样访问方法(调用的时候不用写方法名后的一对括号了)
class Programer():

    hobby = "Play Computer"

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weigth = weight

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weigth

    def self_introduction(self):
        print("My name is %s\nI am %d years old\n" % (self.name, self._age))


if __name__ == "__main__":
    programer = Programer("Albert", 25, 80)
    print(dir(programer))
    print(Programer.get_hobby())
    print(programer.get_weight)
    print(programer.self_introduction())