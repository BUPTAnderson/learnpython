import threading
import time


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    # def __call__(self, *args, **kwargs):
    #     if self._cls not in self._instance:
    #         time.sleep(1)
    #         self._instance_lock.acquire()
    #         try:
    #             if self._cls not in self._instance:
    #                 self._instance[self._cls] = self._cls(*args, **kwargs)
    #         finally:
    #             self._instance_lock.release()
    #     return self._instance[self._cls]
    def __call__(self, *args, **kwargs):
        if self._cls not in self._instance:
            time.sleep(1)
            with self._instance_lock:
                time.sleep(1)
                if self._cls not in self._instance:
                    time.sleep(1)
                    self._instance[self._cls] = self._cls(*args, **kwargs)
        return self._instance[self._cls]


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


def task(arg):
    obj = A(arg)
    print(id(obj))


for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()