import sys
import time
from main_threading import run_threading
from main_multiprocessing import run_multiprocessing
from main_async import run_async

start_time = time.time()

if __name__ == '__main__':
    len_argv = len(sys.argv)
    if len_argv < 2:
        print('No urls specified', 'Usage: python main.py https://some.domain1/uri1 https://some.domain2/uri2', sep='\n')
        exit(1)

    print('You can use different downloadnig options:', '1 - Use threading', '2 - Use multiprocessing', '3 - Use async')
    choice = int(input('Choose download option: '))
    if choice == 1:
        run_threading(sys.argv[1:], start_time)
    elif choice == 2:
        run_multiprocessing(sys.argv[1:], start_time)
    else:
        run_async(sys.argv[1:], start_time)

    print(f'Full processing time is {time.time() - start_time:.2f} seconds')

# Examples
# python ./main_threading.py https://hb.bizmrg.com/frontend-scripts/assets/home/friday-banner/friday-after_desktop.jpg https://gb.ru/_nuxt/img/89f1beb.png https://gb.ru/_nuxt/img/6c757d5.png