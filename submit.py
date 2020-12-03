import sys
import requests
import login
from config import language_dict, source_path

def main(args):
    contest = args[1]
    problem = args[2]
    language = args[3]
    submit(contest, problem, language)

def submit(contest, problem, language):
    # session for submission
    session = requests.session()
    csrf_token = login.login(session)

    # source code
    file = '{}/main.{}'.format(source_path, language_dict[language]['extension'])
    with open(file) as f:
        code = f.read()

    # submission data
    data = {
        'data.TaskScreenName': contest + '_' + problem,
        'data.LanguageId': language_dict[language]['id'],
        'sourceCode': code,
        'csrf_token': csrf_token
    }

    # submit
    print('Submit...', end = ' ')
    url = 'https://atcoder.jp/contests/{}/submit'.format(contest)
    res = session.post(url, data)

    # check response
    message = 'OK!' if res.status_code == 200 else 'Failed.'
    print(message)

if __name__ == '__main__':
    main(sys.argv)
