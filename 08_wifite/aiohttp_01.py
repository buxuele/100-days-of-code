import aiohttp
import asyncio


# why ? charm ? need a def.
async def something():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://beach.cf/') as resp:
            print(resp.status)
            print(await resp.text())

