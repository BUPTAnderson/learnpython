import datetime
a = []
def test(a):
    a.append(1)
    a.append(2)

test(a)
print(a)

a = "other"
access_start = datetime.datetime.now()
# print(access_start)
for i in range(100000):
    if a in ('addFeature'):
        continue

endtime = datetime.datetime.now()
# print(endtime)
print((endtime - access_start).microseconds)

access_start = datetime.datetime.now()
# print(access_start)
for i in range(100000):
    if a == 'addFeature':
        continue

endtime = datetime.datetime.now()
# print(endtime)
print((endtime - access_start).microseconds)
