import sys

import compile
import test
import submit

def main(args):
    problem, language, sub = args[1:]

    if sub != 'f':
        compile.compile(language)
        test.test(problem, language)

    if sub == '' or sub == 'f':
        submit.submit(problem, language)

if __name__ == '__main__':
    main(sys.argv)
