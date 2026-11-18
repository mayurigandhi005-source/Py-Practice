import asyncio
async def Square(n):
    await asyncio.sleep(2)
    return n * n
async def main():
    result = await asyncio.gather (
        Square(2),
        Square(4),
        Square(6)
    )
    print (result)
asyncio.run(main())