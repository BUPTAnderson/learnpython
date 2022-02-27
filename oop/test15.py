import time
import threading

class PipelineStatus:
    def __init__(self):
        self.ts = time.time()

    def update_ts(self, ts):
        self.ts = ts


def update(piplinestatus):
    for i in range(5):
        ts = time.time()
        print(f'thread={threading.current_thread().name},ts={ts}')
        piplinestatus.update_ts(ts)
        time.sleep(1)


if __name__ == '__main__':
    status = PipelineStatus()
    tlist = [threading.Thread(target=update, name=f'LoopThread-{i}', args=(status,)) for i in  range(5)]
    for t in tlist:
        t.start()
    for i in range(5):
        print(f'++++{status.ts}')
        time.sleep(1)