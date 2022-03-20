import time

import blog_spider
import asyncio
import aiohttp

semaphore = asyncio.Semaphore(10)

async def async_craw(url):
    async with semaphore:
        # 都在个信号量的控制范围内
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                # 为了显示明显，每10个爬一次
                await time.sleep(5)
                print(f"craw url{url},{len(result)}")

if __name__ == "__main__":

    loop = asyncio.get_event_loop()

    tasks = [loop.create_task(async_craw(url)) for url in blog_spider.urls]

    start = time.time()
    loop.run_until_complete(asyncio.wait(tasks))
    print("cost time", time.time() - start)
