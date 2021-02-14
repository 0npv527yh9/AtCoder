import sys

import compile
import test
import submit

def main(args):
    problem, language, sub = args[1:]

    compile.compile(language)
    test.test(problem, language)

    if sub == '':
        submit.submit(problem, language)

if __name__ == '__main__':
    main(sys.argv)
