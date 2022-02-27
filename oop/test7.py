import time


class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


# a = Entity("entity")
# a.print_title()
a = "aaa"
b = "bbb"
c = f'+++++++++++++{a}' \
    f'-------------{b}'


def test(a, b, c):
    print("+", a)
    time.sleep(1)
    print("-", b)
    time.sleep(1)
    print("*", c)


test(a, f'+++++++++++++{a}'
         f'-------------{b}', b)