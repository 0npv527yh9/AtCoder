import requests
from bs4 import BeautifulSoup
import sys
from login import login

def submit(session, url, problem):
    # csrf_token取得
    r = session.get(url)
    s = BeautifulSoup(r.text, 'lxml')
    csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

    # source code
    with open('D:/Software/atcoder/src/Main.java') as f:
        source = f.read()

    # submission data
    data = {
        "csrf_token": csrf_token,
        "data.TaskScreenName": problem,
        "data.LanguageId": "4005",
        "sourceCode": source
    }

    # submit
    result = session.post(url, data=data)
    result.raise_for_status()
    if result.status_code==200:
      print("success!")
    else:
      print("failed...")

def submit(url, code):
    session = login()
    res = session.get(url)
    BeautifulSoup(res.text, '')

    # submission data
    data = {
        "csrf_token": csrf_token,
        "data.TaskScreenName": problem,
        "data.LanguageId": "4005",
        "sourceCode": code
    }

def main():
    session = login()
    contest = sys.argv[1]
    problem = contest + '_' + sys.argv[2]
    url = 'https://atcoder.jp/contests/{0}/submit'.format(contest)

    submit(session, url, problem)

if __name__ == '__main__':
    main()
