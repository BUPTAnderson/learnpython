import datetime
a = 1000
b = 2000

c = f'{a - b:d}'
print(c)

access_start = datetime.datetime.now()
# print(access_start)
for i in range(100000):
    c = '%d' % (a + i)

endtime = datetime.datetime.now()
# print(endtime)
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
for i in range(100000):
    c = f'{a + i:d}'

endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
for i in range(100000):
    c = '{}'.format(a + i)

endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)