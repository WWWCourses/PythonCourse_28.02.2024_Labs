from multiprocessing import Pool
import time

def worker(n):
  # for light work, the pool is not efficient, try with n**10
  return n**1000

if __name__ == '__main__':
  t =time.time()

  # create the Pool:
  p = Pool(processes=5)
  result = p.map(worker, range(1_000))
  print(f'Processes Pool result: {result}')
  p.close()
  p.join()

  print("Pool took: ", time.time() - t)

  # serial processing:
  t = time.time()
  result = []
  for x in range(1_000):
    result.append(worker(x))
  # print("Result: ", result)
  print("Serial processing took: ", time.time() - t)