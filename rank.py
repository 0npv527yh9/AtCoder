from sys import argv
from config import language_dict, title, prefix, browser

def main(args):
    problem = args[1].lower()
    language = args[2].lower()
    languageID = language_dict[language]['id']

    url = f'https://atcoder.jp/contests/{title}/submissions?f.Language={languageID}&f.Status=AC&f.Task={prefix}_{problem}&orderBy=time_consumption'
    browser.open(url)

if __name__ == '__main__':
    main(argv)
