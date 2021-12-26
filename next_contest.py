import webbrowser

import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://atcoder.jp'
    html = requests.get(url + '/home').text
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', id='contest-table-upcoming').table
    url += table.tbody.tr.find_all('a')[1]['href']
    webbrowser.open(url)


if __name__ == '__main__':
    main()
