import datetime
result = frozenset({"add_max_waiting_time", "add_max_batch_size", "search_max_waiting_time", "search_max_batch_size"})


def test1(action):
    if action in result:
        return True
    else:
        return False


def test2(action):
    if action in {"add_max_waiting_time", "add_max_batch_size", "search_max_waiting_time", "search_max_batch_size"}:
        return True
    else:
        return False


def test3(action):
    if action in ["add_max_waiting_time", "add_max_batch_size", "search_max_waiting_time", "search_max_batch_size"]:
        return True
    else:
        return False


action = "searchFeatureBatch"
access_start = datetime.datetime.now()
for i in range(100000):
    test1(action)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)
access_start = datetime.datetime.now()
for i in range(100000):
    test2(action)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)
access_start = datetime.datetime.now()
for i in range(100000):
    test3(action)
endtime = datetime.datetime.now()
print((endtime - access_start).microseconds)

if "business" not in result:
    print("++++++++")
if "business" not in result:
    print("--------")
if "add_max_waiting_time" not in result:
    print("============")
