import threading
import time


class TestThread:
    def __init__(self):
        self.name = "a"
        self.m = {"a":"abc", "b":"bbb"}

    def start(self):
        t = threading.Thread(target=self.process, name="check")
        t.daemon = True
        t.start()

    def process(self):
        print("+++++", threading.current_thread().name)
        time.sleep(5)
        self.hello()
        self.m["b"] = "ccc"

    def hello(self):
        print(self.m)


if __name__ == '__main__':
    test = TestThread()
    test.start()
    time.sleep(10)
    # print(test.m)
    print("============")