from bs4 import BeautifulSoup
import config

def login(session):
    url = 'https://atcoder.jp/login'

    print('Login...', end = ' ')
    res = session.get(url)
    bs = BeautifulSoup(res.text, 'lxml')
    csrf_token = bs.select_one("[name = 'csrf_token']").get('value')
    config.login_data['csrf_token'] = csrf_token

    res = session.post(url, config.login_data)

    message = 'OK!' if res.status_code == 200 else 'Failed.'
    print(message)

    return csrf_token
