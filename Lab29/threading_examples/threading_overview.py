import time
import threading


def download_video(url):
    time.sleep(1)
    print(f'{url} is downloaded!')

video_urls = [
    'url1',
    'url2',
    'url3',
    'url4',
    'url5',
]

start = time.time()
threads = []
for url in video_urls:
    tr = threading.Thread(target=download_video, args=(url,))
    tr.start()
    threads.append(tr)


# make sure that all threads are finish their job
for tr in threads:
    tr.join()

time_taken = time.time() - start
print(f'time_taken: {time_taken}')



# sequential time: time_taken: 5.003126382827759