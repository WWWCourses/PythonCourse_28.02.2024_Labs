import multiprocessing as mp


def worker(n):
    # for light work, the pool is not efficient, try with n**10
    res = n**1000
    print(f'res in {mp.current_process().name} = {res}')



if __name__=="__main__":
    process_number = 5
    process_pool = []

    for i in range(process_number):
        pr = mp.Process(target=worker,args=(i,))
        pr.start()
        process_pool.append(pr)


    for pr in process_pool:
        pr.join()

    print('END')
