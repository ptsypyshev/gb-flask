import sys
import requests
import threading
import time

def download(url):
    response = requests.get(url)
    filename = [elem for elem in url.split('/')][-1]
    print(f'Image download time for {filename} is {time.time() - start_time:.2f} seconds')
    with open(filename, "wb") as f:
        f.write(response.content)

threads = []
start_time = time.time()

if __name__ == '__main__':
    len_argv = len(sys.argv)
    if len_argv < 2:
        print('No urls specified', 'Usage: python main.py https://some.domain1/uri1 https://some.domain2/uri2', sep='\n')
        exit(1)

    for url in sys.argv[1:]:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f'Full processing time is {time.time() - start_time:.2f} seconds')

# Examples
# python ./main_threading.py https://hb.bizmrg.com/frontend-scripts/assets/home/friday-banner/friday-after_desktop.jpg https://gb.ru/_nuxt/img/89f1beb.png https://gb.ru/_nuxt/img/6c757d5.png
