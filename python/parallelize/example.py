import time
import threading
import Queue

class Consumer(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            msg = self._queue.get()
            if isinstance(msg,str) and msg == 'quit':
                break

            print "I;m a thread, and i received %s!!" % msg

        print "Bye bye!"

def Producer():
    queue = Queue.Queue()
    worker = Consumer(queue)
    worker.start()

    start_time = time.time()
    while time.time() - start_time < 5:
        queue.put('something at %s' % time.time())
        time.sleep(1)

    queue.put('quit')
    worker.join()

if __name__ == '__main__':
    Producer()

