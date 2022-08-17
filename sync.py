import datetime

import requests


URL = 'https://swapi.dev/'


def get_people(people_id):
    return requests.get(f'{URL}api/people/{people_id}').json()


# print(get_people(1))

def main():
    for i in range(1, 11):
        print(get_people(i))


start = datetime.datetime.now()
main()
print(datetime.datetime.now()-start)