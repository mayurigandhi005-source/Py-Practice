import asyncio

async def greet(name):
    print("Hello", name)
    await asyncio.sleep(2)
    print("Welcome", name)

async def main():
    await asyncio.gather(
        greet("A"),
        greet("B"),
        greet("C")
    )

asyncio.run(main())