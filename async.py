import asyncio
import aiohttp
import datetime

import requests
from more_itertools import chunked

URL = 'https://swapi.dev/'
MAX_CHUNK = 10


def get_len():
    response = requests.get(f'{URL}api/people/')
    # json_data = response.json()
    json_data = response.json()
    return json_data['count']

unit_count = get_len()+1
print(unit_count)


async def check_health(session: aiohttp.ClientSession):
    while True:
        async with session.get(URL) as response:
            print(response.status)


async def get_people(session, people_id):
    async with session.get(f'{URL}api/people/{people_id}') as response:
        json_data = await response.json()
        # await response.close()
        return json_data


async def main():
    unit_list = []
    async with aiohttp.ClientSession() as session:
        # check_health_task = asyncio.create_task(check_health(session))
        coroutines = (get_people(session, i) for i in range(1, unit_count+1))
        for coroutines_chunk in chunked(coroutines, MAX_CHUNK):
            result = await asyncio.gather(*coroutines_chunk)
            for item in result:
                print(item)
                unit_list.append(item)
        # await check_health_task
        print('code after check_health')


# start = datetime.datetime.now()
# # asyncio.run(main())
# asyncio.get_event_loop().run_until_complete(main())
# print(datetime.datetime.now()-start)

start = datetime.datetime.now()
if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())

print(datetime.datetime.now()-start)
