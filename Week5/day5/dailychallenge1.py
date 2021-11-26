import requests
import time
def time_to_load(url):
    response = requests.get(url)
    if response:
        start = time.time()
        requests.get(url)
        end = time.time()
        print(f'{url} took {end-start} seconds to load')
    else:
        print('An error has occurred.')

time_to_load('https://www.google.com/')
time_to_load('https://bodyandsoul.mu/')