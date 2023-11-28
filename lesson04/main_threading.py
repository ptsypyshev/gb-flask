import requests
import threading
import time

def download(url, start_time):
    response = requests.get(url)
    filename = [elem for elem in url.split('/')][-1]
    print(f'Image download time for {filename} is {time.time() - start_time:.2f} seconds')
    with open(filename, "wb") as f:
        f.write(response.content)

threads = []

def run_threading(urls, start_time):
    for url in urls:
        thread = threading.Thread(target=download, args=[url, start_time])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

# Examples
# python ./main_threading.py https://hb.bizmrg.com/frontend-scripts/assets/home/friday-banner/friday-after_desktop.jpg https://gb.ru/_nuxt/img/89f1beb.png https://gb.ru/_nuxt/img/6c757d5.png
