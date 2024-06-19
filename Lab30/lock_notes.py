import threading

def worker():
    global x

    # lock.acquire()
    # try:
    #     x+=1
    # except:
    #     print('An error occured ')
    # finally:
    #     lock.release()

    with lock:
        try:
            x+=1
        except:
            print('An error occured ')

if __name__=="__main__":
    x = 0
    lock = threading.Lock()

    tr1 = threading.Thread(target=worker)
    tr2 = threading.Thread(target=worker)

    tr1.start(x)
    tr2.start(x)
# # е еквивалентно по функционалност на:
# some_lock.acquire()
#   try:
#     # do something...
#   finally:
#     some_lock.release()