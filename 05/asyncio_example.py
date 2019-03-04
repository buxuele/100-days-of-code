import asyncio

# 一个异步的小例子。

async def coroutine_1():
	print("cor 1 is active on the event loop")
	print("cor 1 wait for 4s")
	await asyncio.sleep(4)
	print("cor 1 is back")


async def coroutine_2():
    print("cor 2 is active on the loop")
    print("cor 2 wait for 5s")
    await asyncio.sleep(5)
    print("cor 2 is back")

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(coroutine_1(), coroutine_2()))
