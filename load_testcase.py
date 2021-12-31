import os
import re
import shutil
import sys
import time
from datetime import datetime

from my_requests import AtCoderSession


def main():
    session = AtCoderSession()
    live = len(sys.argv) >= 3
    if live:
        start_hour = int(sys.argv[2])
        start_minute = int(sys.argv[3]) if len(sys.argv) == 4 else 0
        wait_before_starting(start_hour, start_minute)
    url = sys.argv[1]
    url, title, prefix = extract_contest_data(session, url)
    save_contest_data(title, prefix)

    tasks = load_tasks(session, url)
    save_tasks(tasks)


def extract_contest_data(session, url):
    top_page_pattern = 'https://atcoder.jp/contests/([^/]+)'
    task_page_pattern = f'{top_page_pattern}/tasks/(.+)_.+'
    m = re.fullmatch(top_page_pattern, url)
    if m:
        title = prefix = m.groups()[0]
        url = f'{url}/tasks_print'
    else:
        m = re.fullmatch(task_page_pattern, url)
        if m:
            title, prefix = m.groups()
        else:
            print('URL must meet either of the following styles:',
                  f'* {top_page_pattern}',
                  f'* {task_page_pattern}',
                  sep = '\n')
            exit(1)
    return url, title, prefix


def save_contest_data(title, prefix):
    s = f"title = '{title}'\nprefix = '{prefix}'"
    with open('contest.py', 'w') as f:
        f.write(s)


def load_tasks(session, url):
    session.get(url)
    tasks = extract_tasks(session.soup)
    return tasks


def extract_tasks(soup):
    titles = soup.find_all('span', class_ = 'h2')
    tasks = tuple(map(lambda title: title.parent, titles))
    return tasks


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


def extract_samples(task):
    title = task.span.text.strip().split()[0]
    samples = task.find_all(string = re.compile('\s*(入|出)力例 *[0-9]\s*$'))
    samples = tuple(map(extract_sample, samples))
    samples = tuple(zip(samples[::2], samples[1::2]))
    return title, samples


def extract_sample(tag):
    s = tag.parent.parent.find('pre').text
    return s.strip().replace('\r', '') + '\n'


def save_samples(title, samples):
    root = f'../test/{title}'
    if os.path.exists(root):
        shutil.rmtree(root)
    os.makedirs(f'{root}/in')
    os.makedirs(f'{root}/out')
    for i, (in_, out) in enumerate(samples, 1):
        write(f'{root}/in/{i}.txt', in_)
        write(f'{root}/out/{i}.txt', out)


def write(file, s):
    with open(file, 'w', newline = '\n') as f:
        f.write(s)


def wait_before_starting(hour, minute):
    for i in range(2):
        today = datetime.today()
        start = datetime(today.year, today.month, today.day, hour, minute)
        delta = start - today
        wait = max(4, delta.seconds)
        time.sleep(wait)


if __name__ == '__main__':
    main()
