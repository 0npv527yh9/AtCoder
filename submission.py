import requests
from bs4 import BeautifulSoup
import sys
from login import login

language_id_dict = {
       'c': '4001',
     'cpp': '4003',
    'java': '4005',
      'py': '4006'
}

def main(args):
    language = args[1]
    contest = args[2]
    problem = contest + '_' + args[3]
    url = 'https://atcoder.jp/contests/{0}/submit'.format(contest)
    submit(url, language, problem)

def submit(url, language, problem):
    session = requests.session()
    csrf_token = login(session)

    # source code
    file = 'D:/Software/atcoder/src/main.' + language
    with open(file) as f:
        code = f.read()

    # submission data
    data = {
        'data.TaskScreenName': problem,
        'data.LanguageId': language_id_dict[language],
        'sourceCode': code,
        'csrf_token': csrf_token
    }

    # submit
    print('Submit...', end = ' ')
    res = session.post(url, data)

    message = 'OK!' if res.status_code == 200 else 'Failed.'
    print(message)

if __name__ == '__main__':
    main(sys.argv)
