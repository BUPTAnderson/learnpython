# -*- coding: utf-8 -*-
import queue

for i in range(5):
    print(i)

bq = queue.Queue(2)
bq.put("Python")
bq.put("Python")
try:
    bq.put_nowait("Python")
except queue.Full as e:
    print("----------")
    print(type(e))
except Exception as e:
    print(type(e))