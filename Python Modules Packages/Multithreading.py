import asyncio
async def fn():
    print('this is programming')
    await asyncio.sleep(4)
    print('asyc')
    await asyncio.sleep(5)
    print ('not multi-thread')
asyncio.run(fn())    