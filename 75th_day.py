import time
import asyncio
import requests

async def function1():
    # time.sleep(3)
    url = "https://wallpapercave.com/wp/wp7578174.jpg"
    response = requests.get(url)
    open("photo.ico","wb").write(response.content)
    await asyncio.sleep(1)
    print("func 1")
    return "harry"

async def function2():
    # time.sleep(3)
    url = "https://wallpapercave.com/wp/wp7578174.jpg"
    response = requests.get(url)
    open("photo.ico1","wb").write(response.content)
    await asyncio.sleep(1)

    print("func 2")

async def function3():
    # time.sleep(3)
    url = "https://wallpapercave.com/wp/wp7578174.jpg"
    response = requests.get(url)
    open("photo.ico2","wb").write(response.content)
    await asyncio.sleep(4)

    print("func 3")

async def main():
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()
    l = await asyncio.gather(
    function1(),
    function2(),
    function3(),
    
    )
    print(l)

asyncio.run(main())

