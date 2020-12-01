import requests
from bs4 import BeautifulSoup
import sys
from login import login

def main(args):
    contest = args[1]
    problems = 'abcdef' if args[2] == '-' else args[2]
    session = login() if args[3] == 'y' else requests.session()

    url = 'https://atcoder.jp/contests/{0}/tasks/{0}_'.format(contest)

    for problem in problems.upper():
        load_problem(session, url, problem)

def load_problem(session, url, problem):
    path = '../test/' + problem

    parts = get_soup(session, url + problem.lower()).select('.part')

    count = extract_and_output(parts, '入力例', path + '/in')
    extract_and_output(parts, '出力例', path + '/out')

    make_list(count, path)

def get_soup(session, url):
    return BeautifulSoup(session.get(url).text, 'html.parser')

def extract_and_output(result_set, title, path):
    sample_iter = extract_sample(result_set, title)
    count = output_sample(sample_iter, path)
    return count

def extract_sample(result_set, title):
    data = filter(lambda e : title == e.select_one('h3').text[:len(title)], result_set)
    return map(lambda e : e.select_one('pre').text.replace('\r', ''), data)

def output_sample(sample_iter, path):
    for i, sample in enumerate(sample_iter):
        file = '{}/{}.txt'.format(path, i + 1)
        with open(file, 'w', newline = '\n') as f:
            f.write(sample)
    return i + 1

def make_list(count, path):
    sample_list = list(str(i) + '.txt' for i in range(1, count + 1))
    with open(path + '/list.txt', 'w') as f:
        f.write('\n'.join(sample_list))

if __name__ == '__main__':
    main(sys.argv)
