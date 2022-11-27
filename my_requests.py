import pickle
import time

from bs4 import BeautifulSoup
from requests import Session


class AtCoderSession(Session):
    __INTERVAL = 1
    __COOKIES_PICKLE = 'cookies.pickle'
    __LOGIN_URL = 'https://atcoder.jp/login'

    def __init__(self):
        super().__init__()
        self.__timestamp = 0
        self.soup: BeautifulSoup
        try:
            self.__load_cookies()
        except:
            self.__login()

    def __del__(self):
        try:
            self.__save_cookies()
        except:
            pass

    def __login(self):
        login_data = _import_login_data()

        self.get(AtCoderSession.__LOGIN_URL)
        self.csrf_token = self.__find_csrf_token()
        login_data['csrf_token'] = self.csrf_token

        res = self.post(AtCoderSession.__LOGIN_URL, login_data)
        _exit_if_login_failed(res)

    def __find_csrf_token(self):
        return self.soup.find(attrs = {'name': 'csrf_token'}).get('value')

    def __load_cookies(self):
        with open(AtCoderSession.__COOKIES_PICKLE, 'rb') as f:
            data = pickle.load(f)
        self.cookies.update(data[0])
        self.csrf_token = data[1]

    def __save_cookies(self):
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


def _import_login_data():
    try:
        import private
        return private.login_data
    except:
        print('Create "private.py" in the current directory.')
        print(
            'Write "login_data = {\'username\': \'<user name>\', \'password\': \'<password>\'}" in the file.'
        )
        print('Save it.')
        exit(0)


def _exit_if_login_failed(res):
    if BeautifulSoup(res.text, 'lxml').title.text != 'AtCoder':
        print('Sign In failed.')
        print(
            'Please check if "username" and "password" written in "private.py" are correct.'
        )
        exit(0)
