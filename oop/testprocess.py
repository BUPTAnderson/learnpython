import threading
import time
from multiprocessing import Process


def send_process(pipeline_output):
    send_threads = []
    for i in range(8):
        send_t = threading.Thread(target=send_thread, args=(pipeline_output,), name="thread-" + str(i))
        send_t.daemon = True
        send_threads.append(send_t)
        send_t.start()
    for t in send_threads:
        print("--------->", t.name)
        t.join()


def send_thread(pipeline_output):
    i = 0
    # while True:
    for j in range(10):
        result = threading.current_thread().name + "-" + str(i)
        print(result)
        i += 1
        time.sleep(1)


if __name__ == '__main__':
    process = Process(target=send_process, args=("aaa",))
    process.daemon = True
    process.start()

    time.sleep(11)
    # print(test.m)
    print("============")