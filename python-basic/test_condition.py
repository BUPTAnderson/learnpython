# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 17:15:29 2018

@author: 18665
"""

import threading
import time

con = threading.Condition()
class Producer(threading.Thread):
    # 生产者函数
    def run(self):
        time.sleep(1)
        with con:
            print("P get lock")
            time.sleep(5)
        print("P release")
        time.sleep(5)
        print("P return")



class Consumer(threading.Thread):
    # 消费者函数
    def run(self):
        with con:
            print("C get lock")
            time.sleep(5)
            print("C relases lock")
        print("C reutrn")

# count = 500



def test():
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()

def test2():
    p = Producer()
    p.start()
    c = Consumer()
    c.start()
if __name__ == '__main__':
    test2()
    time.sleep(100)
