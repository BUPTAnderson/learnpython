class A():
    def __init__(self):
        print('A class called')

class B(A):
    def __init__(self):
        print('B class called')
        A.__init__(self)
class C(A):
    def __init__(self):
        print('C class called')
        A.__init__(self)
class D(B,C):
    def __init__(self):
        print('D class called')
        B.__init__(self)
        C.__init__(self)
d = D()