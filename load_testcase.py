import json
import os
import re
import shutil
import sys
import time
from datetime import datetime

import config
from my_requests import AtCoderSession


def main():
    session = AtCoderSession()

    # Wait until the contest starts if you participate it in.
    live = len(sys.argv) >= 3
    if live:
        start_hour = int(sys.argv[2])
        start_minute = int(sys.argv[3]) if len(sys.argv) == 4 else 0
        wait_before_starting(start_hour, start_minute)

    # Load and save meta-information.
    url = sys.argv[1]
    url, title, prefix = extract_contest_data(url)

    # Load and save testcases.
    tasks = load_tasks(session, url)
    save_tasks(tasks, title, prefix)


# Extract contest meta-information from url.
def extract_contest_data(url):
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
            print('URL must meet either of the following styles:')
            print(f'* {top_page_pattern}')
            print(f'* {task_page_pattern}')
            exit(1)

    return url, title, prefix


# GET and parse the tasks page.
def load_tasks(session, url):
    session.get(url)
    tasks = extract_tasks(session.soup)
    return tasks


# Extract tasks from BeautifulSoup
def extract_tasks(soup):
    titles = soup.find_all('span', class_ = 'h2')
    tasks = tuple(map(lambda title: title.parent, titles))
    return tasks


# Save the testcases.
def save_tasks(tasks, contest_title, contest_prefix):
    loaded = []
    failed = []
    for task in tasks:
        title = task.span.text.strip().split()[0]
        try:
            samples = extract_samples(task)
            save_samples(title, samples)
            loaded.append(title)
        except:
            failed.append(title)

    save_contest_data(contest_title, contest_prefix, loaded)
    print('loaded:', *loaded)
    print('failed:', *failed)


# Save contest meta-information in "contest.py".
def save_contest_data(title, prefix, tasks):
    try:
        d = json.load(open(config.task_info_file))
    except:
        d = {}
    for task in tasks:
        task = task.lower()
        if task not in d:
            d[task] = {}
        d[task]['title'] = title
        d[task]['prefix'] = prefix
    json.dump(d, open(config.task_info_file, 'w'))


# Extract the testcases from the task html.
def extract_samples(task):
    samples = task.find_all(string = re.compile('\s*(入|出)力例 *[0-9]\s*$'))
    samples = tuple(map(extract_sample, samples))
    samples = tuple(zip(samples[::2], samples[1::2]))
    return samples


def extract_sample(tag):
    s = tag.parent.parent.find('pre').text
    return s.strip().replace('\r', '') + '\n'


# Save the testcases.
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
    today = datetime.today()
    start = datetime(today.year, today.month, today.day, hour, minute)
    delta = start - today
    wait = max(0, delta.seconds) + 10
    time.sleep(wait)


if __name__ == '__main__':
    main()
