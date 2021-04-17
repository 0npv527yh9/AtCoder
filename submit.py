import sys
import webbrowser

from config import language_dict, source_path
from contest import title, prefix
from my_requests import AtCoderSession

def main(args):
    problem = args[1]
    language = args[2]

    submit(problem, language)

def submit(problem, language):
    # session for submission
    session = AtCoderSession()

    # source code
    code = load_code(language)

    # submission data
    data = {
        'data.TaskScreenName': prefix + '_' + problem,
        'data.LanguageId': language_dict[language]['id'],
        'sourceCode': code,
        'csrf_token': session.csrf_token
    }

    # submit
    url = f'https://atcoder.jp/contests/{title}/submit'
    session.post(url, data)

    # the browser opens submissions page
    open_submissions_page()

def load_code(language):
    extension = language_dict[language]['extension']
    file = f'{source_path}/main.{extension}'
    with open(file, encoding = 'utf-8') as f:
        code = f.read()
    return code

def open_submissions_page():
    url = f'https://atcoder.jp/contests/{title}/submissions/me'
    webbrowser.open(url)

if __name__ == '__main__':
    main(sys.argv)
