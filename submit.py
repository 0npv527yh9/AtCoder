import sys
import webbrowser

from config import language_dict, source_path, option_dict
from my_requests import AtCoderSession

def main():
    language, task = sys.argv[1:3]
    option_dict.update(language = language, task = task)
    submit(option_dict)

def submit(option_dict):
    # session for submission
    session = AtCoderSession()

    # source code
    language = option_dict['language']
    code = load_code(language)

    # submission data
    data = {
        'data.TaskScreenName': option_dict['prefix'] + '_' + option_dict['task'],
        'data.LanguageId': language_dict[language]['id'],
        'sourceCode': code,
        'csrf_token': session.csrf_token
    }

    # submit
    title = option_dict['title']
    url = f'https://atcoder.jp/contests/{title}/submit'
    session.post(url, data)

    # the browser opens submissions page
    open_submissions_page(title)


def load_code(language):
    extension = language_dict[language]['extension']
    file = f'{source_path}/main.{extension}'
    with open(file, encoding = 'utf-8') as f:
        code = f.read()
    return code


def open_submissions_page(title):
    url = f'https://atcoder.jp/contests/{title}/submissions/me'
    webbrowser.open(url)


if __name__ == '__main__':
    main()
