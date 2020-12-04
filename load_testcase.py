import sys
import requests
from bs4 import BeautifulSoup
import login

def main(args):
    contest = args[1]
    problems = 'ABCDEF' if args[2] == '-' else args[2]
    session = requests.session()
    if args[3] == 'y':
        login.login(session)

    url = 'https://atcoder.jp/contests/{0}/tasks/{0}_'.format(contest)

    for problem in problems.upper():
        load_problem(session, url, problem)

def load_problem(session, url, problem):
    test_home = '../test/' + problem

    parts = create_soup(session, url + problem.lower()).select('.part')
    num = extract_and_output(parts, '入力例', test_home + '/in')
    extract_and_output(parts, '出力例', test_home + '/out')

    make_list(num, test_home)
    print(problem, num)

def create_soup(session, url):
    return BeautifulSoup(session.get(url).text, 'lxml')

def extract_and_output(result_set, title, path):
    sample_iter = extract_sample(result_set, title)
    num = output_sample(sample_iter, path)
    return num

def extract_sample(result_set, title):
    data = filter(lambda e : title == e.select_one('h3').text[:len(title)], result_set)
    return map(lambda e : e.select_one('pre').text.replace('\r', ''), data)

def output_sample(sample_iter, path):
    for i, sample in enumerate(sample_iter, 1):
        file = '{}/{}.txt'.format(path, i)
        with open(file, 'w', newline = '\n') as f:
            f.write(sample)
    return i

def make_list(count, path):
    sample_list = list(str(i) + '.txt' for i in range(1, count + 1))
    with open(path + '/list.txt', 'w') as f:
        f.write('\n'.join(sample_list))

if __name__ == '__main__':
    main(sys.argv)
