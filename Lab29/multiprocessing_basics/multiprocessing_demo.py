import time
import multiprocessing


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

if __name__ == '__main__':
    start = time.time()
    processes = []
    for url in video_urls:
        pr = multiprocessing.Process(target=download_video, args=(url,))
        pr.start()
        processes.append(pr)


    # make sure that all processes are finish their job
    for pr in processes:
        pr.join()

    time_taken = time.time() - start
    print(f'time_taken: {time_taken}')



# sequential time: time_taken: 5.003126382827759