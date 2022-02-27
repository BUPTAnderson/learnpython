import datetime
class AA:
    def __init__(self, no):
        self.sex = 'Male'
        self.no = no

    def hello(self):
        print(f'sex:{self.sex}, no:{self.no}')


a_list = [AA(i) for i in range(10)]
access_start = datetime.datetime.now()
for a in a_list:
    for i in range(10000):
        r = 'sex:{}, no:{}'.format(a.sex, a.no)
    # print(a.no)
    # a.hello()
endtime = datetime.datetime.now()
# print(endtime)
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
for a in a_list:
    for i in range(10000):
        r= f'sex:{a.sex}, no:{a.no}'
endtime = datetime.datetime.now()
# print(endtime)
print((endtime - access_start).microseconds)

print('action={}'.format('len'))