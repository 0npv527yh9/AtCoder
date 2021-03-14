import sys
from time import sleep
from os.path import exists
from os import mkdir
from shutil import rmtree

import requests
from bs4 import BeautifulSoup

import login
from config import register_contest

def main(args):
    title = args[1]
    problems = args[2]
    session = requests.session()

    needs_login = False
    prefix = title.replace('-', '_')

    i = 3
    while i < len(args):
        if args[i] == '-l':
            needs_login = True
        elif args[i] == '-p':
            i += 1
            prefix = args[i]
        i += 1

    if needs_login:
        login.login(session)

    url = f'https://atcoder.jp/contests/{title}/tasks/{prefix}_'

    for problem in problems.upper():
        load_problem(session, url, problem)
        sleep(2)

    register_contest(title, prefix)

def load_problem(session, url, problem):
    test_home = '../test/' + problem
    if exists(test_home):
        rmtree(test_home)
    mkdir(test_home)

    parts = create_soup(session, url + problem.lower()).select('.part')
    num = extract_and_output(parts, '入力例', test_home + '/in')
    extract_and_output(parts, '出力例', test_home + '/out')

    make_list(num, test_home)
    print(problem, num)

def create_soup(session, url):
    try:
        res = session.get(url)
        res.raise_for_status()
        return BeautifulSoup(res.text, 'lxml')
    except Exception as e:
        print(e)
        sys.exit(res.status_code)

def extract_and_output(result_set, title, path):
    sample_iter = extract_sample(result_set, title)
    num = output_sample(sample_iter, path)
    return num

def extract_sample(result_set, title):
    match_title = lambda e : title == e.select_one('h3').text[:len(title)]
    data = filter(match_title, result_set)
    extract_sample = lambda e : e.select_one('pre').text.lstrip().replace('\r', '')
    return map(extract_sample, data)

def output_sample(sample_iter, path):
    mkdir(path)
    for i, sample in enumerate(sample_iter, 1):
        file = f'{path}/{i}.txt'
        with open(file, 'w', newline = '\n') as f:
            f.write(sample)
    return i

def make_list(count, path):
    sample_list = list(f'{i}.txt' for i in range(1, count + 1))
    sample_list_str = '\n'.join(sample_list)
    with open(f'{path}/list.txt', 'w') as f:
        f.write(sample_list_str)

if __name__ == '__main__':
    main(sys.argv)
