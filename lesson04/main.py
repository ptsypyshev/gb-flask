import asyncio
import sys
import aiofiles
import aiohttp
import time

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = [elem for elem in url.split('/')][-1]
                print(f'Image download time for {filename} is {time.time() - start_time:.2f} seconds')
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await response.read())
                await f.close()

async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)

start_time = time.time()

if __name__ == '__main__':
    len_argv = len(sys.argv)
    if len_argv < 2:
        print('No urls specified', 'Usage: python main.py https://some.domain1/uri1 https://some.domain2/uri2', sep='\n')
        exit(1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))
    print(f'Full processing time is {time.time() - start_time:.2f} seconds')

# Examples
# python ./main.py https://hb.bizmrg.com/frontend-scripts/assets/home/friday-banner/friday-after_desktop.jpg https://gb.ru/_nuxt/img/89f1beb.png https://gb.ru/_nuxt/img/6c757d5.png
