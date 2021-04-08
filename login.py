from time import sleep
from pickle import dump

import requests
from bs4 import BeautifulSoup

from config import login_data

INTERVAL = 10

def main():
    url = 'https://atcoder.jp/login'
    session = requests.session()
    csrf_token = load_csrf_token(session, url)
    sleep(INTERVAL)
    login(session, url, csrf_token)
    save('cookies.pickle', session.cookies)

def load_csrf_token(session, url):
    res = session.get(url)
    bs = BeautifulSoup(res.text, 'lxml')
    csrf_token = bs.find(attrs = {'name': 'csrf_token'}).get('value')
    return csrf_token

def login(session, url, csrf_token):
    login_data['csrf_token'] = csrf_token
    res = session.post(url, data = login_data)
    res.raise_for_status()
    print(res.reason)

def save(file, obj):
    with open(file, 'wb') as f:
        dump(obj, f)

if __name__ == '__main__':
    main()
