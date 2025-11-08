import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):
        total = sum(range(1000000))
        print(f'{self.name} computed sum: {total}')

if __name__ == '__main__':
    for _ in range(10):
        process = MyProcess()
        process.start()
        process.join()
