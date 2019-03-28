# when: 2019/03/25 8:09 PM
# who: fanchuang
# repo: https://github.com/buxuele/
# find: baogebuxuele@163.com

"""about:
1. 

"""

import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, "http://httpbin.org/get")
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())





