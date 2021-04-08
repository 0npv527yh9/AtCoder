import sys
from time import sleep, time
from os.path import exists
from os import mkdir
from shutil import rmtree
import re

from bs4 import BeautifulSoup

from login import login
from config import register_contest, session

timestamp = 0
INTERVAL = 2

def main(args):
    url = args[1]
    url, title, prefix = extract_contest_data(session, url)
    register_contest(title, prefix)

    tasks = load_tasks(session, url)
    save_tasks(tasks)

def extract_contest_data(session, url):
    top_page_pattern = 'https://atcoder.jp/contests/([^/]+)'
    task_page_pattern = f'{top_page_pattern}/tasks/(.+)_.+'
    if (m := re.fullmatch(top_page_pattern, url)):
        title = m.groups()[0]
        # login(session)
        prefix = load_prefix(session, f'{url}/tasks')
        url = f'{url}/tasks_print'
    elif (m := re.fullmatch(task_page_pattern, url)):
        title, prefix = m.groups()
    else:
        print('URL must meet either of the following styles:',
              f'* {top_page_pattern}',
              f'* {task_page_pattern}',
              sep = '\n')
        exit(1)
    return url, title, prefix

def load_prefix(session, url):
    bs = create_soup(session, url)
    url = bs.find('h2').parent.a.get('href')
    prefix = re.findall('([^/]+)_', url)[0]
    return prefix

def load_tasks(session, url):
    bs = create_soup(session, url)
    tasks = extract_tasks(bs)
    return tasks

def create_soup(session, url):
    stamp()
    res = session.get(url)
    res.raise_for_status()
    return BeautifulSoup(res.text, 'lxml')

def stamp():
    global timestamp
    t = time()
    wait = max(0, INTERVAL - (t - timestamp))
    sleep(wait)
    timestamp = t

def save_tasks(tasks):
    loaded = []
    failed = []
    for task in tasks:
        try:
            title, samples = extract_samples(task)
            save_samples(title, samples)
            loaded.append(title)
        except:
            failed.append(title)
    print('loaded:', *loaded)
    print('failed:', *failed)

def extract_tasks(bs):
    titles = bs.find_all('span', class_ = 'h2')
    tasks = tuple(map(lambda title : title.parent, titles))
    return tasks

def extract_samples(task):
    title = task.span.text.strip()[0]
    samples = task.find_all(string = re.compile('(入|出)力例 *[0-9]'))
    samples = map(extract_sample, samples)
    samples = tuple(samples)
    samples = tuple(zip(samples[::2], samples[1::2]))
    return title, samples

def extract_sample(tag):
    s = tag.parent.find_next_sibling('pre').text
    return s.strip().replace('\r', '') + '\n'

def save_samples(title, samples):
    root = f'../test/{title}'
    if exists(root):
        rmtree(root)
    mkdir(root)
    mkdir(f'{root}/in')
    mkdir(f'{root}/out')
    for i, (in_, out) in enumerate(samples, 1):
        write(f'{root}/in/{i}.txt', in_)
        write(f'{root}/out/{i}.txt', out)
    make_list(i, root)

def write(file, s):
    with open(file, 'w', newline = '\n') as f:
        f.write(s)

def make_list(count, path):
    sample_list = list(f'{i}.txt' for i in range(1, count + 1))
    sample_list_str = '\n'.join(sample_list)
    with open(f'{path}/list.txt', 'w') as f:
        f.write(sample_list_str)

if __name__ == '__main__':
    main(sys.argv)
