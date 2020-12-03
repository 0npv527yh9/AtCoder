from bs4 import BeautifulSoup
from config import login_data

url = 'https://atcoder.jp/login'

def login(session):
    # get csrf_token
    print('Login...', end = ' ')
    res = session.get(url)
    bs = BeautifulSoup(res.text, 'lxml')
    csrf_token = bs.select_one("[name = 'csrf_token']").get('value')
    login_data['csrf_token'] = csrf_token

    # post login data
    res = session.post(url, login_data)

    # check response
    message = 'OK!' if res.status_code == 200 else 'Failed.'
    print(message)

    return csrf_token
