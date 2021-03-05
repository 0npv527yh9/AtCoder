from sys import argv
from config import title, prefix
import webbrowser

def main(args):
    problem = args[1]
    url = f'https://atcoder.jp/contests/{title}/tasks/{prefix}_{problem}'
    webbrowser.open(url)

if __name__ == '__main__':
    main(argv)
