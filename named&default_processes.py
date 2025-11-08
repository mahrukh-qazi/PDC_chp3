import multiprocessing
import time

def myFunc():
    name = multiprocessing.current_process().name
    total = sum(range(1000000))
    print(f"{name} computed sum: {total}")
    time.sleep(3)

if __name__ == '__main__':
    named_process = multiprocessing.Process(name='myFunc_process', target=myFunc)
    default_process = multiprocessing.Process(target=myFunc)

    named_process.start()
    default_process.start()

    named_process.join()
    default_process.join()
