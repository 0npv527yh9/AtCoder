import sys

import compile
import test
import submit

def main(args):
    problem, language, sub = args[1:]

    if sub != 'f':
        compile.compile(language)
        AC = test.test(problem, language)
        sub = sub == '' and AC

    if sub:
        submit.submit(problem, language)

if __name__ == '__main__':
    main(sys.argv)
