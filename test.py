import os
import re
import shutil
import subprocess
import sys

from config import language_dict

col, row = shutil.get_terminal_size()


def main():
    problem = sys.argv[1].upper()
    language = sys.argv[2].lower()
    test(problem, language)


def test(problem, language):
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
            print_diff(sample_file, trim(input_), trim(expected),
                       f'{trim(output)}\n\n{error}')
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
    l = s.split('\n')
    h = row - 1 >> 1
    l = l[:h] + ['...'] + l[-h:] if row < len(l) else l
    lw = col - 3 >> 1
    rw = col - 3 - lw
    l = list(map(lambda s: s
                 if col >= len(s) else s[:lw] + '...' + s[-rw:], l))
    s = '\n'.join(l)
    return s


if __name__ == '__main__':
    main()
