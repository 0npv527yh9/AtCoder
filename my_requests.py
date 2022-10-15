import pickle
import time

from bs4 import BeautifulSoup
from requests import Session

from private import login_data


class AtCoderSession(Session):
    __INTERVAL = 10
    __COOKIES_PICKLE = 'cookies.pickle'
    __LOGIN_URL = 'https://atcoder.jp/login'

    def __init__(self, login = False):
        super().__init__()
        self.__timestamp = 0
        self.soup = None
        if login:
            self.__login()
        else:
            self.__load()

    def __del__(self):
        self.__save()
        print('Session was saved.')

    def __login(self):
        self.get(AtCoderSession.__LOGIN_URL)
        self.csrf_token = self.__find_csrf_token()
        login_data['csrf_token'] = self.csrf_token
        self.post(AtCoderSession.__LOGIN_URL, login_data)

    def __find_csrf_token(self):
        return self.soup.find(attrs = {'name': 'csrf_token'}).get('value')

    def __load(self):
        with open(AtCoderSession.__COOKIES_PICKLE, 'rb') as f:
            data = pickle.load(f)
        self.cookies.update(data[0])
        self.csrf_token = data[1]

    def __save(self):
        data = (self.cookies, self.csrf_token)
        with open(AtCoderSession.__COOKIES_PICKLE, 'wb') as f:
            pickle.dump(data, f)

    def get(self, url):
        self.__wait()
        res = super().get(url)
        self.soup = BeautifulSoup(res.text, 'lxml')
        return res

    def __wait(self):
        now = time.time()
        dt = now - self.__timestamp
        t = max(0, AtCoderSession.__INTERVAL - dt)
        time.sleep(t)
        self.__timestamp = now

    def post(self, url, data):
        res = super().post(url, data)
        res.raise_for_status()
        print(res.reason)
