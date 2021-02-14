import sys
import requests
import login
from config import language_dict, source_path, title, prefix

def main(args):
    problem = args[1]
    language = args[2]

    submit(problem, language)

def submit(problem, language):
    # session for submission
    session = requests.session()
    csrf_token = login.login(session)

    # source code
    file = '{}/main.{}'.format(source_path, language_dict[language]['extension'])
    with open(file) as f:
        code = f.read()

    # submission data
    data = {
        'data.TaskScreenName': prefix + '_' + problem,
        'data.LanguageId': language_dict[language]['id'],
        'sourceCode': code,
        'csrf_token': csrf_token
    }

    # submit
    print('Submit...', end = ' ')
    url = f'https://atcoder.jp/contests/{title}/submit'
    res = session.post(url, data)

    # check response
    message = 'OK!' if res.status_code == 200 else 'Failed.'
    print(message)

    # the browser opens submissions page 
    open_submissions_page()

def open_submissions_page():
    url = f'https://atcoder.jp/contests/{title}/submissions/me'
    browser.open(url)

if __name__ == '__main__':
    main(sys.argv)
