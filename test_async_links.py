import asyncio
import aiohttp
import time

with open("links.txt", "r") as fread:
    links = fread.readlines()


print("Am gasit:", len(links))

# links = links[:200]


async def fetch(session:aiohttp.ClientSession, url):
    async with session.get(url) as response:
        # return response.status 
        return response.status

async def scrape_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(fetch(session, url))
        results =  await asyncio.gather(*tasks)

        return results
    


if __name__ == "__main__":
    start_time = time.time()
    status_codes = asyncio.run(scrape_urls(links))
    stop_time = time.time()
    print(f"Functia s-a executat in {stop_time - start_time} secunde.")
    print(status_codes)