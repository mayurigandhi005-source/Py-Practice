import asyncio
async def task(name):
    print(f"{name} start")
    await asyncio.sleep(2)
    print(f"{name} completed") 

async def main():
    await asyncio.gather (
        task("task 1"),
        task("task 2"),
        task("task 3")
    )  
asyncio.run(main())       