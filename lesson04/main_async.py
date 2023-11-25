import asyncio
import aiofiles
import aiohttp
import time

async def download(url, start_time):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                filename = [elem for elem in url.split('/')][-1]
                print(f'Image download time for {filename} is {time.time() - start_time:.2f} seconds')
                f = await aiofiles.open(filename, mode='wb')
                await f.write(await response.read())
                await f.close()

async def main(urls, start_time):
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url, start_time))
        tasks.append(task)
    await asyncio.gather(*tasks)

def run_async(urls, start_time):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls, start_time))

# Examples
# python ./main.py https://hb.bizmrg.com/frontend-scripts/assets/home/friday-banner/friday-after_desktop.jpg https://gb.ru/_nuxt/img/89f1beb.png https://gb.ru/_nuxt/img/6c757d5.png
