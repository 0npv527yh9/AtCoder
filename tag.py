import os
import sys
import time
import webbrowser

import requests
from bs4 import BeautifulSoup


def main():
    url = sys.argv[1]

    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    arrange(soup)
    html = str(soup)
    show(html)


def filter_abc(soup):
    tbodies = soup.find_all('tbody')
    abc = []
    for tbody in tbodies:
        try:
            if tbody.tr.strong.text[:3] == 'abc':
                abc.append(tbody.tr)
        except:
            pass

    return abc


def arrange(soup):
    abc = filter_abc(soup)

    soup.clear()
    soup.append(soup.new_tag('table'))
    soup.table.append(soup.new_tag('tbody'))
    tbody = soup.tbody

    for i, tr in enumerate(abc, 1):
        tds = tr.find_all('td')

        tds[0].string = str(i)
        tds[2].a.string = tds[1].a.strong.string.upper(
        ) + ' ' + tds[2].a.b.string[3:]

        tr.clear()
        for td in (tds[0], tds[2]):
            del td['scope']
            tr.append(td)

        tbody.append(tr)


def show(html):
    file = os.getcwd().replace('\\', '/') + '/' + 'temp.html'
    write(file, html)
    path = f'file://{file}'
    webbrowser.open(path)
    time.sleep(1)
    os.remove(file)


def write(file, s):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(s)


if __name__ == '__main__':
    main()
