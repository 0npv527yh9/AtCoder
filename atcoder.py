import sys
import test

import compile
import submit
from config import option_dict
from load_testcase import save_contest_data


def main():
    language, task = sys.argv[1:3]
    option_dict.update(language = language, task = task)
    load_option_dict(option_dict, sys.argv[3:])

    if option_dict['test']:
        compile.compile(language)
        AC = test.test(language, task)
        option_dict['submit'] &= AC

    if option_dict['submit']:
        submit.submit(option_dict)


def load_option_dict(option_dict, args):
    args = iter(args)
    while True:
        try:
            mode = next(args)
        except:
            break

        if mode == 't':
            option_dict['task'] = next(args)
        elif mode == 'p':
            option_dict['prefix'] = next(args)
            save_contest_data(option_dict['title'], option_dict['prefix'])
        elif mode == 'f':
            option_dict['test'] = False
        elif mode == 'n':
            option_dict['submit'] = False
        else:
            raise Exception('Invalid option: ' + mode)


if __name__ == '__main__':
    main()
