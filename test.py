import os
import re
import shutil
import subprocess
import sys

from config import language_dict

col, row = shutil.get_terminal_size()


def main():
    language = sys.argv[1].lower()
    problem = sys.argv[2].upper()
    test(language, problem)


def test(language, problem):
    test_home = '../test/' + problem

    sample_file_list = sorted(os.listdir(test_home + '/in'))

    AC = True

    for sample_file in sample_file_list:
        input_file = test_home + '/in/' + sample_file
        output_file = test_home + '/out/' + sample_file

        output, error = execute(language, input_file)
        expected = read(output_file)

        if expected != output:
            input_ = read(input_file)
            print_diff(
                sample_file, trim(input_), trim(expected),
                f'{trim(output)}\n\n{error}'
            )
            AC = False
            if error:
                break

    if AC:
        print('AC')

    return AC


def read(file):
    with open(file) as f:
        return f.read().strip()


def execute(language, input_file):
    command = language_dict[language]['execute']
    option = {'stdin': open(input_file), 'capture_output': True}
    res = subprocess.run(command, **option)
    out = res.stdout.decode()
    out = re.sub(' *\r?\n', '\n', out).strip()
    err = res.stderr.decode().strip()

    return out, err


def print_diff(file, input_, expected, actual):
    title_tuple = ('input', 'expected', 'actual')
    content_tuple = (input_, expected, actual)

    print_title(file, '=')
    for title, content in zip(title_tuple, content_tuple):
        print_title(title)
        print(content)
    print('\n')


def print_title(title, style = '-'):
    print(title.center(col, style))


def trim(s):
    rows = s.split('\n')
    h = row - 1 >> 1
    rows = rows[:h] + ['...'] + rows[-h:] if row < len(rows) else rows
    lw = col - 3 >> 1
    rw = col - 3 - lw
    rows = list(
        map(
            lambda row: row
            if col >= len(row) else row[:lw] + '...' + row[-rw:], rows
        )
    )
    s = '\n'.join(rows)
    return s


if __name__ == '__main__':
    main()
