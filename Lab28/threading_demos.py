import threading
import time

def worker():
    time.sleep(1)
    print(f'Worker is called in thread {threading.current_thread().name}')



tr1 = threading.Thread( target=worker )
tr2 = threading.Thread( target=worker )

start=time.time()
tr1.start()
tr2.start()

tr1.join()
tr2.join()

end = time.time()

print(f'time: {end-start}')


# 1
# 2
# Worker is called1
