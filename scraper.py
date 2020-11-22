import requests
from bs4 import BeautifulSoup as bs
import numpy as np

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

url = 'https://nine.websudoku.com/'
grid = []


def scrape():

    r = requests.get(url, headers=headers)
    r = r.content
    soup = bs(r, 'html.parser')

    table = soup.find('table', id='puzzle_grid')
    attributes = table.find_all('input')

    i = 0
    temp = []
    for sq in attributes:
        if i % 9 == 0:
            temp = []
            grid.append(temp)
            i = 0
        try:
            temp.append(int(sq['value']))
        except Exception as e:
            temp.append(int(0))
        i += 1

    print(np.matrix(grid))
    print()