import multiprocessing as mp
import time

def increment(r):
  # global x
  x = queue.get()

  print(f'x in process {mp.current_process().name} = {x}')

  for _ in r:
    x+=1

  # save to queue incrememnted x:
  queue.put(x)
  print(f"x in {mp.current_process().name}: {x}")


if __name__ == "__main__":
  MAX_RANGE = 100_000_000
  # x = 0

  start = time.time()

  queue = mp.Queue()
  queue.put(0)

  pr1 = mp.Process(target=increment, args=(range(MAX_RANGE),))
  pr2 = mp.Process(target=increment, args=(range(MAX_RANGE),))
  pr1.start();pr2.start();
  pr1.join();pr2.join();

  x = queue.get()
  time_taken = time.time() - start
  print(f"x in {mp.current_process().name}: {x}")
  print(time_taken)
