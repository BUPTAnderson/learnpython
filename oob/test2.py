class Programer():
    hobby = "Play Computer" # 被该类的所有对象共享

    def __init__(self, name, age, weight): # python没有访问控制，没有提供私有属性的功能，全靠自觉
        self.name = name        # 约定：public
        self._age = age         # 约定： private
        self.__weight = weight  # 私有属性，实际是python自动在该属性前加上_${类名}，这里是_Programer__weight

    def get_weight(self):
        return self.__weight


if __name__ == "__main__":
    programer = Programer("Albert", 25, 80)
    # print(programer.hobby)
    print(dir(programer))       # 打印所有属性
    print(programer.__dict__)   # 打印从构造函数获得的属性
    print(programer.get_weight())
    print(programer._Programer__weight)
    # programer2 = Programer("Steven", 18, 70)
    # print(programer2.hobby)