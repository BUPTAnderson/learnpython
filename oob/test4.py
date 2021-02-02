# 类的继承
# 单继承 class B(A):
# 多继承 class C(A,B):
from test3 import Programer


class BackendProgramer(Programer):

    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language


if __name__ == '__main__':
    programer = BackendProgramer("Albert", 25, 80, "python")
    print(dir(programer))
    print(programer.__dict__)
    print(type(programer))
    print(isinstance(programer, Programer))
