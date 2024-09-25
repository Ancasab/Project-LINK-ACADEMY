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
