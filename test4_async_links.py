# "url = https://realpython.com/python-async-features/"; "  example_6.py program"

# import asyncio
# import aiohttp
# from codetiming import Timer

# async def task(name, work_queue):
#     timer = Timer(text=f"Task {name} elapsed time: {{:.1f}}")
#     async with aiohttp.ClientSession() as session:
#         while not work_queue.empty():
#             url = await work_queue.get()
#             print(f"Task {name} getting URL: {url}")
#             timer.start()
#             async with session.get(url) as response:
#                 await response.text()
#             timer.stop()

# async def main():
#     """
#     This is the main entry point for the program
#     """
#     # Create the queue of work
#     work_queue = asyncio.Queue()

#     # Put some work in the queue
#     for url in [
#         "http://google.com",
#         "http://yahoo.com",
#         "http://linkedin.com",
#         "http://apple.com",
#         "http://microsoft.com",
#         "http://facebook.com",
#         "http://twitter.com",
#     ]:
#         await work_queue.put(url)

#     # Run the tasks
#     with Timer(text="\nTotal elapsed time: {:.1f}"):
#         await asyncio.gather(
#             asyncio.create_task(task("One", work_queue)),
#             asyncio.create_task(task("Two", work_queue)),
#         )

# if __name__ == "__main__":
#     asyncio.run(main())

# Here’s what’s happening in this program:

# Line 2 imports the aiohttp library, which provides an asynchronous way to make HTTP calls.
# Line 3 imports the the Timer code from the codetiming module.
# Line 5 marks task() as an asynchronous function.
# Line 6 creates the Timer instance used to measure the time taken for each iteration of the task loop.
# Line 7 creates an aiohttp session context manager.
# Line 8 creates an aiohttp response context manager. It also makes an HTTP GET call to the URL taken from work_queue.
# Line 11 starts the timer instance
# Line 12 uses the session to get the text retrieved from the URL asynchronously.
# Line 13 stops the timer instance and outputs the elapsed time since timer.start() was called.
# Line 39 creates a Timer context manager that will output the elapsed time the entire while loop took to execute.
import pytest
import asyncio
import aiohttp
import time

with open("links.txt", "r") as fread:
    links = fread.readlines()


print("Numarul de link-uri gasit:", len(links))



async def fetch(session:aiohttp.ClientSession, url):
    async with session.get(url) as response:
        return response.status

async def scrape_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        results =  await asyncio.gather(*tasks)

        return results
    
def test_response():
    status_codes = asyncio.run(scrape_urls(links))
    assert all([status == 200 for status in status_codes])




if __name__ == "__main__":
    start_time = time.time()
    status_codes = asyncio.run(scrape_urls(links))
    stop_time = time.time()
    print(f"Functia s-a executat in {stop_time - start_time} secunde.")
    print(status_codes)
    
    print("Toate status_code sunt egale cu 200: ", all([status == 200 for status in status_codes]))
