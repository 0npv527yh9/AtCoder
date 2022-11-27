import sys
import webbrowser

from config import language_dict
from contest import prefix, title


def main(args):
    task = args[1].lower()
    language = args[2].lower()
    languageID = language_dict[language]['id']

    url = f'https://atcoder.jp/contests/{title}/submissions?f.Language={languageID}&f.Status=AC&f.Task={prefix}_{task}&orderBy=time_consumption'
    webbrowser.open(url)


if __name__ == '__main__':
    main(sys.argv)
