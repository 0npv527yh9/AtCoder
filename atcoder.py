import sys
import compile
import test
import submit

def main(args):
    contest = args[1]
    problem = args[2]
    language = args[3]

    compile.compile(language)

    test.test(problem, language)

    submit.submit(contest, problem, language)

if __name__ == '__main__':
    main(sys.argv)
