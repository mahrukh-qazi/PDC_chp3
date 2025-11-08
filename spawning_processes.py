import multiprocessing

def myFunc(i):
    total = sum(range(1000000))
    print(f'Process {i} computed sum: {total}')

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i,))
        process.start()
        process.join()
