import multiprocessing
import random
import time

class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        for _ in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print(f'Producer added item {item} to queue {self.name}')
            time.sleep(1)
            print(f'Queue size: {self.queue.qsize()}')

class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if self.queue.empty():
                print('Queue is empty')
                break
            item = self.queue.get()
            print(f'Consumer popped item {item} by {self.name}')
            time.sleep(2)

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
