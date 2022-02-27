class Student:
    def __init__(self):
        print("student init")

    @property
    def get_score(self):
        return self._score

    @get_score.setter
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


class Master(Student):
    # def __init__(self):
    #     self.__b__ = 10
    #     super(Master, self).__init__()
        # print("Master")

    def __hello__(self):
        print("hello master")

    def __len__(self):
        return 3

# s = Student()
# print(s.__dir__())
# s.set_score = 60  # ok!
# print(s.get_score)
master = Master()
# print(master.__b__)
print(len(master))
# hello(master)
