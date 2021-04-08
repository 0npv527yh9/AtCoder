from time import time, sleep
from pickle import load, dump

from requests import Session
from bs4 import BeautifulSoup

from config import login_data

class AtCoderSession(Session):
    __INTERVAL = 10
    __COOKIES_PICKLE = 'cookies.pickle'
    __LOGIN_URL = 'https://atcoder.jp/login'

    def __init__(self, login = False):
        super().__init__()
        self.__timestamp = 0
        self.__soup = None
        if login:
            self.__login()
        else:
            self.cookies = AtCoderSession.__load_cookies()

    def __login(self):
        csrf_token = self.__load_csrf_token()
        login_data['csrf_token'] = csrf_token
        self.post(AtCoderSession.__LOGIN_URL, login_data)

    def __load_csrf_token(self):
        self.get(AtCoderSession.__LOGIN_URL)
        csrf_token = self.__soup.find(attrs = {'name': 'csrf_token'}).get('value')
        return csrf_token

    def __load_cookies():
        with open(AtCoderSession.__COOKIES_PICKLE, 'rb') as f:
            cookies = load(f)
        return cookies

    def save_cookies(self):
        with open(AtCoderSession.__COOKIES_PICKLE, 'wb') as f:
            dump(self.cookies, f)

    def get(self, url):
        self.__wait()
        res = super().get(url)
        self.__soup = BeautifulSoup(res.text, 'lxml')
        return res

    def __wait(self):
        now = time()
        dt = now - self.__timestamp
        t = max(0, AtCoderSession.__INTERVAL - dt)
        sleep(t)
        self.__timestamp = now

    def post(self, url, data):
        res = super().post(url, data)
        res.raise_for_status()
        print(res.reason)

    def write(self, file):
        s = str(self.__soup)
        with open(file, 'w', encoding = 'utf-8') as f:
            f.write(s)
