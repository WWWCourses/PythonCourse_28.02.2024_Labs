import threading
import multiprocessing
import time


def worker(num):
    global x;
    print(f'Worker {num} starting')
    # Simulate some work
    time.sleep(2)
    x+=1

    print(f'Worker {num} done')


def consequently():
    start = time.time()
    for i in range(5):
        worker(i)

    end = time.time()
    print(f'concequently execution time: {end-start}')

def threading_demo():
    start = time.time()
    threads = []

    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.time()
    print(f'threaded execution time: {end-start}')

def multiprocessing_demo():
    start = time.time()
    processes = []

    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.time()
    print(f'multiprocessing execution time: {end-start}')

if __name__ == '__main__':
    x = 0
    concequently()
    print(f'X after concequently: {x}')
    threading_demo()
    print(f'X after threading_demo: {x}')
    multiprocessing_demo()
    print(f'X after multiprocessing_demo: {x}')

