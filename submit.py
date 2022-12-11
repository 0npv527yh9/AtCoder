import sys
import webbrowser

from config import language_dict
from my_requests import AtCoderSession


def submit(option_dict):
    session = AtCoderSession()

    language = option_dict['language']
    code = load_code(language)
    contest_info = option_dict['contest_info']

    # submission data
    data = {
        'data.TaskScreenName':
            contest_info['prefix'] + '_' + option_dict['task'],
        'data.LanguageId':
            language_dict[language]['id'],
        'sourceCode':
            code,
        'csrf_token':
            session.csrf_token
    }

    # submit
    title = contest_info['title']
    url = f'https://atcoder.jp/contests/{title}/submit'
    session.post(url, data)

    # the browser opens submissions page
    open_submissions_page(title)


# Load the source code written in "language".
def load_code(language):
    file = language_dict[language]['file']
    with open(file, encoding = 'utf-8') as f:
        code = f.read()
    return code


def open_submissions_page(title):
    url = f'https://atcoder.jp/contests/{title}/submissions/me'
    webbrowser.open(url)
