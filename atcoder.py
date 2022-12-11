import json
import sys
import test

import compile
import config
import submit


def main():
    # Load info
    language, task = sys.argv[1:3]
    option_dict = {
        'language': language,
        'task': task,
        'test': True,
        'submit': True,
        'contest_info': json.load(open(config.task_info_file))[task]
    }
    load_options(option_dict, sys.argv[3:])

    # Compile and Test
    if option_dict['test']:
        compile.compile(language)
        AC = test.test(language, task)
        option_dict['submit'] &= AC

    # Submit
    if option_dict['submit']:
        submit.submit(option_dict)
        print('Submitted')


def load_options(option_dict, args):
    args = iter(args)
    while True:
        try:
            mode = next(args)
        except:
            break

        if mode == 't':
            option_dict['task'] = next(args)
        elif mode == 'f':
            option_dict['test'] = False
        elif mode == 'n':
            option_dict['submit'] = False
        else:
            print('Invalid option: ' + mode)
            exit(0)


if __name__ == '__main__':
    main()
